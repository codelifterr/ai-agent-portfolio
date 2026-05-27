from __future__ import annotations

import json
import sys
from pathlib import Path

from .tools import checklist_tool, notes_tool
from .workflows import AgentStep, AgentWorkflow

TOOLS = {"notes": notes_tool, "checklist": checklist_tool}


def load_workflow(path: Path) -> AgentWorkflow:
    data = json.loads(path.read_text(encoding="utf-8"))
    steps = [AgentStep(**step) for step in data["steps"]]
    return AgentWorkflow(goal=data["goal"], steps=steps, tools=TOOLS)


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python3 -m agent_portfolio.cli examples/research_brief.json")
        return 2
    workflow = load_workflow(Path(argv[0]))
    result = workflow.run()
    print(result.final_summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
