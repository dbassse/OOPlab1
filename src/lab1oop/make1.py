from .task_package_1.zad1 import Pair


def main() -> None:
    """Демонстрация работы класса Pair"""
    a = Pair(1.2, 2.4)
    a.display()
    print("Расстояние от начала координат до точки:: ", a.distance())
    a.read()
    a.display()
    a.make_pair(10.2, 14.4)
    a.display()


if __name__ == "__main__":
    main()
