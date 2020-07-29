class Road:
    _length: int
    _width: int

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calculate(self, mass: int, depth: int):
        return int((self._length * self._width * mass * depth) / 1000)


length, width, mass, depth = [int(x) for x in input(
    "Через пробел введите длину(в метрах), ширину(в метрах), массу (в кг) и толщину полотна (в см): ").split()]

road = Road(length, width)
result = road.calculate(mass, depth)

print(f"Понадобится {result} тонн(ы) асфальта для покрытия всего дорожного полотна")