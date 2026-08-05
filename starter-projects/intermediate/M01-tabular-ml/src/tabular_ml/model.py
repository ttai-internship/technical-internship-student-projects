from collections import Counter


class MajorityClassifier:
    """A deliberately simple baseline for a classification task."""

    def fit(self, y):
        counts = Counter(int(value) for value in y)
        if not counts:
            raise ValueError("cannot fit on empty labels")
        self.label_ = counts.most_common(1)[0][0]
        return self

    def predict(self, rows):
        if not hasattr(self, "label_"):
            raise RuntimeError("fit must be called before predict")
        return [self.label_] * len(rows)


def build_student_model():
    """Student Core: return one non-trivial, documented model."""
    raise NotImplementedError("add a model such as LogisticRegression")
