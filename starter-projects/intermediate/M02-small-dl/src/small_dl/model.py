from torch import nn


class TinyMLP(nn.Module):
    def __init__(self, hidden_size: int = 8) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, 2),
        )

    def forward(self, features):
        return self.network(features)


def build_student_model():
    """Student Core: change one documented model or training choice."""
    return TinyMLP(hidden_size=8)
