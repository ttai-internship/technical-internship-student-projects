import argparse
import json

from .agent import RandomAgent, q_learning
from .env import GridWorld
from .evaluate import evaluate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", choices=["random", "q-learning"], default="random")
    parser.add_argument("--episodes", type=int, default=10)
    args = parser.parse_args()

    env = GridWorld()
    if args.agent == "random":
        agent = RandomAgent()
        policy = agent.act
    else:
        policy = q_learning(env, episodes=args.episodes)
    print(json.dumps(evaluate(env, policy, episodes=args.episodes), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
