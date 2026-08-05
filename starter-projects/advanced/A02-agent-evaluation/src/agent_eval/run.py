import json

from .cases import CASES
from .metrics import evaluate


def main() -> int:
    print(json.dumps(evaluate(CASES), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
