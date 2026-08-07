def total_price(price: float, quantity: int) -> float:
    return price * quantity


def receipt(name: str, price: float, quantity: int) -> str:
    total = total_price(price, quantity)
    return f"{name}: {total:.2f}"


def main() -> None:
    print(receipt("notebook", 12.5, 2))


if __name__ == "__main__":
    main()
