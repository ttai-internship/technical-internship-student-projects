import random
from collections.abc import Callable

from .env import RIGHT, Action, GridWorld


class RandomAgent:
    def __init__(self, seed: int = 7) -> None:
        self.random = random.Random(seed)

    def act(self, _state: tuple[int, int]) -> Action:
        return self.random.randrange(4)


def q_learning(
    env: GridWorld,
    episodes: int = 100,
    alpha: float = 0.1,
    gamma: float = 0.95,
    epsilon: float = 0.2,
    seed: int = 7,
) -> Callable[[tuple[int, int]], Action]:
    """Student Core: implement a tabular Q-learning policy."""
    del env, episodes, alpha, gamma, epsilon, seed
    return lambda _state: RIGHT
