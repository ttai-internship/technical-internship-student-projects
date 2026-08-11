"""Run a deterministic scaled dot-product attention micro-reproduction."""

from __future__ import annotations

import json

import numpy as np


def attention(
    query: np.ndarray, key: np.ndarray, value: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    scores = query @ key.T / np.sqrt(query.shape[-1])
    scores = scores - scores.max(axis=-1, keepdims=True)
    weights = np.exp(scores)
    weights = weights / weights.sum(axis=-1, keepdims=True)
    return weights @ value, weights


def run() -> dict[str, object]:
    query = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    key = query.copy()
    value = np.array([[1.0, 0.0], [0.0, 2.0], [3.0, 3.0]])
    output, weights = attention(query, key, value)
    return {
        "pack_id": "transformer-micro",
        "sequence_length": int(query.shape[0]),
        "attention_shape": list(weights.shape),
        "row_sums": weights.sum(axis=1).round(8).tolist(),
        "output": output.round(8).tolist(),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
