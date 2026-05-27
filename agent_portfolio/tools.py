from __future__ import annotations


def notes_tool(instruction: str) -> str:
    """Return a compact note for a step.

    In a real agent this could be replaced with search, email, GitHub,
    database, or browser tools.
    """
    return f"note:{instruction.strip()}"


def checklist_tool(instruction: str) -> str:
    items = [item.strip() for item in instruction.split(";") if item.strip()]
    return "checklist:" + ", ".join(f"[ ] {item}" for item in items)
