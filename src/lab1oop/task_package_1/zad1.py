import math


class Pair:
    """Координаты first и second по умолчанию равны
    позиции началу координат, имеется проверка
    на правильность введенного дробного числа"""

    def __init__(self, first: float = 0.0, second: float = 0.0) -> None:
        try:
            self.first = float(first)
            self.second = float(second)
        except (ValueError, TypeError) as e:
            raise ValueError("Введите дробное число Float") from e

    def read(self) -> None:
        try:
            self.first = float(input("Введите первую координату x: "))
            self.second = float(input("Введите вторую координату y: "))
        except ValueError as e:
            raise ValueError("Введите число!") from e

    def display(self) -> None:
        print(f"Координаты точки х и y: ({self.first}, {self.second})")

    def distance(self) -> float:
        return math.sqrt(self.first**2 + self.second**2)

    def make_pair(self, first: float, second: float) -> None:
        self.first = first
        self.second = second


if __name__ == "__main__":
    point = Pair(1.2, 2.4)
    point.display()
    print("Расстояние от начала координат до точки: ", point.distance())
    point.read()
    point.display()
    point.make_pair(10.2, 14.4)
    point.display()
