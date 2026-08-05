import unittest

from rl_control.env import DOWN, RIGHT, GridWorld


class RLControlPublicTests(unittest.TestCase):
    def test_reset_and_step(self) -> None:
        env = GridWorld(size=2, max_steps=5)
        self.assertEqual(env.reset(), (0, 0))
        state, reward, done = env.step(RIGHT)
        self.assertEqual(state, (0, 1))
        self.assertEqual(reward, -1.0)
        self.assertFalse(done)

    def test_goal_is_terminal(self) -> None:
        env = GridWorld(size=2, max_steps=5)
        env.reset()
        env.step(DOWN)
        state, reward, done = env.step(RIGHT)
        self.assertEqual(state, (1, 1))
        self.assertEqual(reward, 10.0)
        self.assertTrue(done)


if __name__ == "__main__":
    unittest.main()
