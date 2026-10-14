# Azure AI Agent Platform

A local-first AI agent platform built to understand and demonstrate core Azure AI concepts without requiring paid Azure resources.

## Learning Notes

- **Agent orchestration:** The agent directs requests to the appropriate tool or model.
- **Tool calling:** Tools let an agent perform specific actions instead of only generating text.
- **Testing:** Automated tests help verify agent behaviour and catch regressions.
- **Dependency injection:** The agent can receive a model or tool instead of creating a fixed one internally.
- **Rule-based routing:** The current agent uses a keyword check to direct status requests to its status tool.