from sklearn.metrics import accuracy_score, confusion_matrix


def evaluate(model, features, labels) -> dict:
    predictions = model.predict(features)
    return {
        "accuracy": float(accuracy_score(labels, predictions)),
        "confusion_matrix": confusion_matrix(labels, predictions).tolist(),
        "count": len(labels),
    }
