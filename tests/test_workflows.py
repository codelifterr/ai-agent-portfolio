from agent_portfolio.tools import notes_tool
from agent_portfolio.workflows import AgentStep, AgentWorkflow


def test_workflow_runs_all_steps():
    workflow = AgentWorkflow(
        goal="demo",
        steps=[AgentStep("step_one", "collect info")],
        tools={"notes": notes_tool},
    )
    result = workflow.run()
    assert result.completed_steps == ["step_one"]
    assert "collect info" in result.final_summary
