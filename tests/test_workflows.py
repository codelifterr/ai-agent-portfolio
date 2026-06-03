import unittest

from agent_portfolio.tools import notes_tool
from agent_portfolio.workflows import AgentStep, AgentWorkflow


class WorkflowTest(unittest.TestCase):
    def test_workflow_runs_all_steps(self):
        workflow = AgentWorkflow(
            goal="demo",
            steps=[AgentStep("step_one", "collect info")],
            tools={"notes": notes_tool},
        )
        result = workflow.run()
        self.assertEqual(result.completed_steps, ["step_one"])
        self.assertIn("collect info", result.final_summary)


if __name__ == "__main__":
    unittest.main()
