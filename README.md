# AI Agent Portfolio

Small Python examples that demonstrate AI-agent workflow design, task planning, tool-use concepts, evidence collection, and final summaries.

This is a compact technical project: the workflow runner is intentionally simple so the control flow is easy to inspect.

## What is inside

- A minimal workflow runner
- Reusable task and tool abstractions
- Example workflows for research, planning, and evaluation
- Simple tests that document expected behavior
- JSON input examples for repeatable local runs

## Project structure

```text
agent_portfolio/
  cli.py        # CLI entry point
  workflows.py  # workflow runner and result model
  tools.py      # simple example tools
examples/
  research_brief.json
  evaluation_review.json
tests/
  test_workflows.py
```

## Run locally

```bash
python3 -m agent_portfolio.cli examples/research_brief.json
python3 -m agent_portfolio.cli examples/evaluation_review.json
```

## Run tests

```bash
python3 -m unittest discover -s tests -p 'test*.py'
```

## Example workflow idea

```text
Goal: prepare a short research brief
1. collect notes
2. identify risks or missing evidence
3. summarize next actions
```

## Why this project exists

Agent workflows are easier to trust when the steps, tools, and evidence are visible. This project shows a small pattern for making that flow explicit.

## License

MIT
