from .task_package_2.zad2 import Fraction


def main() -> None:
    frac = Fraction(1, 8)
    frac.display()

    frac.read()
    frac.display()

    print(f"Сложение: {frac + 1.2}")
    print(f"Сложение: {frac - 1.2}")
    print(f"Умножение: {frac * 1}")
    print(f"Меньше чем: {frac < 1.3}")
    print(f"Меньше или равно: {frac <= 23}")
    print(f"Больше чем: {frac > 43}")
    print(f"Больше или равно: {frac >= 1}")


if __name__ == "__main__":
    main()
