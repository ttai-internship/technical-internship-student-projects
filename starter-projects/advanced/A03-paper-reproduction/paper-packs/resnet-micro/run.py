"""Run a deterministic residual-learning mechanism micro-reproduction."""

from __future__ import annotations

import json

import numpy as np


def plain_block(x: np.ndarray, weight: np.ndarray) -> np.ndarray:
    return np.tanh(x @ weight)


def residual_block(x: np.ndarray, weight: np.ndarray) -> np.ndarray:
    return x + np.tanh(x @ weight)


def run() -> dict[str, object]:
    rng = np.random.default_rng(7)
    x = rng.normal(size=(6, 4))
    weight = rng.normal(scale=0.2, size=(4, 4))
    plain = plain_block(x, weight)
    residual = residual_block(x, weight)
    return {
        "pack_id": "resnet-micro",
        "seed": 7,
        "input_shape": list(x.shape),
        "plain_output_shape": list(plain.shape),
        "residual_output_shape": list(residual.shape),
        "residual_delta_l2": float(np.linalg.norm(residual - x)),
        "plain_l2": float(np.linalg.norm(plain)),
        "residual_l2": float(np.linalg.norm(residual)),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
