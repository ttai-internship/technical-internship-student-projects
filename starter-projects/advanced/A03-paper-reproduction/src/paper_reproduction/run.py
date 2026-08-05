import argparse
import json

from .experiment import make_data, run_variant


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=["baseline", "student"], default="baseline")
    args = parser.parse_args()
    print(json.dumps(run_variant(make_data(), args.variant), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
