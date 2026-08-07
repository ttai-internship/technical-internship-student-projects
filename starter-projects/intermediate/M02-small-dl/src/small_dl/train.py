import argparse
import json

import torch
import torch.nn as nn

from .data import make_loader
from .model import build_student_model


def train(epochs: int = 3, learning_rate: float = 0.05, return_model: bool = False) -> dict:
    torch.manual_seed(7)
    model = build_student_model()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    loss_fn = nn.CrossEntropyLoss()
    history = []
    for epoch in range(epochs):
        total_loss = 0.0
        for features, labels in make_loader():
            optimizer.zero_grad()
            loss = loss_fn(model(features), labels)
            loss.backward()
            optimizer.step()
            total_loss += float(loss.item())
        history.append({"epoch": epoch + 1, "loss": total_loss})
    result = {"history": history, "final_loss": history[-1]["loss"]}
    if return_model:
        result["model"] = model
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(train(args.epochs), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
