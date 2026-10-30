import sys
import json
import re

class PrdSynthesizer:
    @staticmethod
    def synthesize(title, objective, target_users, key_features):
        user_stories = []
        for i, feat in enumerate(key_features, 1):
            user_stories.append({
                "id": f"US-{i:03d}",
                "as_a": target_users[0] if target_users else "User",
                "i_want": f"to {feat}",
                "so_that": "I can achieve seamless productivity and reliability",
                "acceptance_criteria": [
                    f"Given authenticated user, when invoking {feat}, then response status is 200",
                    "Latency should not exceed 500ms p95",
                    "Telemetry events logged to central bus"
                ]
            })

        endpoints = [f"/actions/{re.sub(r'[^a-zA-Z0-9]', '-', f).lower()}" for f in key_features]

        return {
            "title": title,
            "objective": objective,
            "target_audience": target_users,
            "user_stories": user_stories,
            "api_contract_skeleton": {
                "base_path": f"/api/v1/{title.lower().replace(' ', '-')}",
                "endpoints": endpoints
            }
        }

def handle_rpc(request):
    method = request.get("method")
    req_id = request.get("id")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "synthesize_prd",
                        "description": "Synthesize a structured PRD with user stories and API contracts.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "objective": {"type": "string"},
                                "target_users": {"type": "array", "items": {"type": "string"}},
                                "key_features": {"type": "array", "items": {"type": "string"}}
                            },
                            "required": ["title", "objective", "key_features"]
                        }
                    }
                ]
            }
        }

    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "synthesize_prd":
            res = PrdSynthesizer.synthesize(
                args.get("title", "Project"),
                args.get("objective", ""),
                args.get("target_users", ["User"]),
                args.get("key_features", [])
            )
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res)}]}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()
