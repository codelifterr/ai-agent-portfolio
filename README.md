# AI Agent Portfolio

Small Python examples for AI agent workflow design, task planning, and tool-use concepts.

## What is inside

- A minimal workflow runner
- Reusable task and tool abstractions
- Example workflows for research, planning, and evaluation
- Simple tests that document expected behavior

## Run locally

```bash
python3 -m agent_portfolio.cli examples/research_brief.json
```

## Project structure

```text
agent_portfolio/
  cli.py
  workflows.py
  tools.py
examples/
  research_brief.json
tests/
  test_workflows.py
```

## Example idea

The project models an agent as a workflow:

1. receive a goal
2. break it into steps
3. choose tools
4. collect evidence
5. produce a verified result

This is intentionally lightweight and easy to read.
