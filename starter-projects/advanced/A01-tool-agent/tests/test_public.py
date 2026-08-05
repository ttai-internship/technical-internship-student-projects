import unittest

from tool_agent.agent import ToolAgent
from tool_agent.fake_model import fake_model
from tool_agent.tools import list_tools


class ToolAgentPublicTests(unittest.TestCase):
    def test_fake_model_can_call_a_tool(self) -> None:
        agent = ToolAgent(list_tools(), fake_model)
        self.assertIn("open", agent.run("ticket: 1"))
        self.assertEqual(agent.logs[-1]["tool"], "get_ticket")

    def test_plain_answer_does_not_call_a_tool(self) -> None:
        agent = ToolAgent(list_tools(), fake_model)
        self.assertIn("without", agent.run("hello"))
        self.assertNotIn("tool", agent.logs[-1])


if __name__ == "__main__":
    unittest.main()
