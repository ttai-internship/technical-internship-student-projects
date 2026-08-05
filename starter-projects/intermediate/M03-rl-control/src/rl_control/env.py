from dataclasses import dataclass


Action = int
UP, DOWN, LEFT, RIGHT = range(4)


@dataclass
class GridWorld:
    size: int = 4
    max_steps: int = 30

    def reset(self) -> tuple[int, int]:
        self.position = (0, 0)
        self.steps = 0
        return self.position

    def step(self, action: Action) -> tuple[tuple[int, int], float, bool]:
        if not hasattr(self, "position"):
            self.reset()
        row, column = self.position
        if action == UP:
            row -= 1
        elif action == DOWN:
            row += 1
        elif action == LEFT:
            column -= 1
        elif action == RIGHT:
            column += 1
        else:
            raise ValueError("action must be 0, 1, 2, or 3")

        row = max(0, min(self.size - 1, row))
        column = max(0, min(self.size - 1, column))
        self.position = (row, column)
        self.steps += 1
        reached_goal = self.position == (self.size - 1, self.size - 1)
        timed_out = self.steps >= self.max_steps
        return self.position, (10.0 if reached_goal else -1.0), reached_goal or timed_out
