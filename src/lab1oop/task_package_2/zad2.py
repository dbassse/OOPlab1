from typing import Union


class Fraction:
    def __init__(self, integer: int = 0, fractional: int = 0) -> None:
        self.integer = integer
        self.fractional = fractional

    @property
    def value(self) -> float:
        return float(f"{self.integer}.{self.fractional}")

    def read(self) -> None:
        try:
            self.integer = int(input("Введите целую часть: "))
            self.fractional = int(input("Введите дробную часть: "))
        except ValueError as e:
            raise ValueError("Должны быть введены целые числа!") from e

    def display(self) -> None:
        print(f"Итоговое число из целой и дробной части: {self.value}")

    def __add__(self, other: Union["Fraction", float, int]) -> float:
        if isinstance(other, Fraction):
            return self.value + other.value
        return self.value + other

    def __sub__(self, other: Union["Fraction", float, int]) -> float:
        if isinstance(other, Fraction):
            return self.value - other.value
        return self.value - other

    def __mul__(self, other: Union["Fraction", float, int]) -> float:
        if isinstance(other, Fraction):
            return self.value * other.value
        return self.value * other

    def __lt__(self, other: Union["Fraction", float, int]) -> bool:
        if isinstance(other, Fraction):
            return self.value < other.value
        return self.value < other

    def __le__(self, other: Union["Fraction", float, int]) -> bool:
        if isinstance(other, Fraction):
            return self.value <= other.value
        return self.value <= other

    def __gt__(self, other: Union["Fraction", float, int]) -> bool:
        if isinstance(other, Fraction):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other: Union["Fraction", float, int]) -> bool:
        if isinstance(other, Fraction):
            return self.value >= other.value
        return self.value >= other

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Fraction):
            return self.value == other.value
        if isinstance(other, (int, float)):
            return self.value == other
        return False

    def __str__(self) -> str:
        return f"Fraction({self.integer}, {self.fractional}) = {self.value}"


if __name__ == "__main__":
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
