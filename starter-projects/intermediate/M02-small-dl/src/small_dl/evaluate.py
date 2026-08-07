from pathlib import Path

import torch


def evaluate(model, loader) -> dict:
    """Evaluate classification accuracy without updating model parameters."""
    model.eval()
    correct = 0
    count = 0
    with torch.no_grad():
        for features, labels in loader:
            predictions = model(features).argmax(dim=1)
            correct += int((predictions == labels).sum().item())
            count += int(labels.numel())
    return {"accuracy": correct / count if count else 0.0, "count": count}


def save_checkpoint(model, path: str | Path) -> Path:
    """Save a state-dict checkpoint and return its resolved destination."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), destination)
    return destination
