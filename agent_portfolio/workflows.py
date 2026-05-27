from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable

Tool = Callable[[str], str]


@dataclass(frozen=True)
class AgentStep:
    """One step in a simple agent workflow."""

    name: str
    instruction: str
    tool: str = "notes"


@dataclass
class WorkflowResult:
    goal: str
    completed_steps: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    final_summary: str = ""


class AgentWorkflow:
    """A tiny workflow runner for demonstrating agent task orchestration."""

    def __init__(self, goal: str, steps: Iterable[AgentStep], tools: dict[str, Tool]):
        self.goal = goal
        self.steps = list(steps)
        self.tools = tools

    def run(self) -> WorkflowResult:
        result = WorkflowResult(goal=self.goal)
        for step in self.steps:
            if step.tool not in self.tools:
                raise KeyError(f"Missing tool: {step.tool}")
            output = self.tools[step.tool](step.instruction)
            result.completed_steps.append(step.name)
            result.evidence.append(output)
        result.final_summary = self._summarize(result.evidence)
        return result

    def _summarize(self, evidence: list[str]) -> str:
        joined = " | ".join(evidence)
        return f"Goal: {self.goal}
Evidence: {joined}
Status: completed"
