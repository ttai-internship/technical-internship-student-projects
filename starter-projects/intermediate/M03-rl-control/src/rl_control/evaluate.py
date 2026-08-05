from collections.abc import Callable

from .env import Action, GridWorld


def run_episode(env: GridWorld, policy: Callable[[tuple[int, int]], Action]) -> float:
    state = env.reset()
    total = 0.0
    while True:
        state, reward, done = env.step(policy(state))
        total += reward
        if done:
            return total


def evaluate(env: GridWorld, policy, episodes: int = 10) -> dict:
    rewards = [run_episode(env, policy) for _ in range(episodes)]
    return {
        "episodes": episodes,
        "rewards": rewards,
        "average_reward": sum(rewards) / episodes,
    }
