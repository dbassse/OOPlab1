class Ship:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.cargo = 0  # начальный груз - 0 тонн

    def load_cargo(self, weight: int) -> None:
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight: int) -> None:
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")


# Пример использования класса:
# Создаем корабль грузоподъемностью 100 тонн
ship = Ship("Black Pearl", 100)

# Пытаемся загрузить 50 тонн
ship.load_cargo(50)  # Вывод: Loaded 50 tons

# Пытаемся загрузить еще 60 тонн (превысит лимит)
ship.load_cargo(60)  # Вывод: Cannot load that much

# Разгружаем 30 тонн
ship.unload_cargo(30)  # Вывод: Unloaded 30 tons

# Пытаемся разгрузить больше, чем есть на борту
ship.unload_cargo(30)  # Вывод: Cannot unload that much
