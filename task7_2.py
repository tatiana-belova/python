from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def count_cloth(self):
        pass


class Coat(Clothes):
    @property
    def count_cloth(self):
        print(f"Расход ткани для пошива пальто: {round(self.size/6.5 + 0.5, 3)}м.")
        return self.size/6.5 + 0.5


class Suit(Clothes):
    @property
    def count_cloth(self):
        print(f"Расход ткани для пошива костюма: {round(2 * self.size + 0.3, 3)}м.")
        return 2 * self.size + 0.3


while True:
    try:
        h = float(input("Введите ваш рост в метрах (Например: 1.89): "))
        v = float(input("Введите ваш размер одежды (российский): "))

        print(f"Общий расход ткани для пошива пальто и костюма: {round(Coat(v).count_cloth + Suit(h).count_cloth,3)}м.")

        break

    except ValueError:
        print("Введите целое или дробное число.")