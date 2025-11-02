from typing import List


class River:
    # Список всех рек (классическая переменная)
    all_rivers: List["River"] = []

    def __init__(self, name: str, length: int) -> None:
        self.name = name
        self.length = length
        # Добавляем текущую реку в список всех рек
        River.all_rivers.append(self)


# Создание объектов рек (должно быть ВНЕ тела класса)
volga = River("Волга", 3530)
seine = River("Сена", 776)
nile = River("Нил", 6852)

# Печать всех названий рек
for river in River.all_rivers:
    print(river.name)

# Вывод:
# Волга
# Сена
# Нил
