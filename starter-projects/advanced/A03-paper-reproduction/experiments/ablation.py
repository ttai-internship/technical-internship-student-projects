from paper_reproduction.experiment import make_data, run_variant


def run() -> dict:
    return run_variant(make_data(seed=7, size=20), "student")


if __name__ == "__main__":
    print(run())
