---
name: agents
---

# Custom Agents Reference

This file documents custom agent configuration and usage for this workspace.

## Purpose

- Define custom agent behavior for workspace-specific automation.
- Provide a central reference for agent triggers, descriptions, and intended usage.

## Usage

- Add custom agent files with `.agent.md` extension in this repository when you need a specialized workflow.
- Use `description` statements to make the agent discoverable by keywords like `agent`, `workflow`, `automation`, or `custom task`.

## Example Agent File Structure

```md
---
name: my-custom-agent
source: workspace
description: "Use when you want to run a custom multi-step coding workflow."
---

# My Custom Agent

This agent performs step-by-step tasks with restricted scope and tool usage.
```

## Notes

- For workspace-wide instructions, consider adding `copilot-instructions.md` or `.github/AGENTS.md` if this workspace is shared.
- Keep descriptions clear and specific so the agent can be found by the chat system.
