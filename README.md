# PRD & Technical Spec Synthesizer Skill for Autonomous Agents

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](requirements.txt)

Enterprise-grade Product Requirement Document (PRD) and technical specification synthesizer for autonomous agents. Automatically compiles high-level project goals into user stories with Gherkin acceptance criteria, edge cases, and OpenAPI-compatible contract skeletons.

## Core Capabilities
- **Structured User Story Decomposition**: Transforms user intents into standardized user stories (As a / I want / So that).
- **Gherkin Acceptance Criteria**: Synthesizes verifiable criteria with latency and telemetry invariants.
- **API Contract Generation**: Automatically designs REST endpoint routes and contract schemas.

## MCP Server Integration
Run standard stdio MCP server:
```bash
python mcp_server.py
```

### Available MCP Tools
- `synthesize_prd`: Generate structured PRD and user stories from high-level features.
- `generate_api_contract`: Produce endpoint skeletons from feature specifications.
