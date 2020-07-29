class Car:
    name = "Машина"
    color = "Черный"
    speed = 90
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость = {self.speed}")


class TownCar(Car):
    def __init__(self):
        print("Это городская машина")

    def show_speed(self):
        speed = 60
        print(f"Текущая скорость = {self.speed}")
        if self.speed > speed:
            print(f"Внимание! Вы превышаете скорость на {self.speed - speed}")


class SportCar(Car):
    def __init__(self):
        print("Это спортивная машина")


class WorkCar(Car):
    def __init__(self):
        print("Это грузовая машина")

    def show_speed(self):
        speed = 40
        print(f"Текущая скорость = {self.speed}")
        if self.speed > speed:
            print(f"Внимание! Вы превышаете скорость на {self.speed - speed}")


class PoliceCar(Car):
    is_police = True

    def __init__(self):
        print("Это полицейская машина")


town_car_1 = TownCar()
print(town_car_1.name)
print(town_car_1.color)
town_car_1.show_speed()
town_car_1.speed = 60
town_car_1.show_speed()

print('')

sport_car_1 = SportCar()
sport_car_1.name = "Ferrari"
sport_car_1.color = "Желтый"
sport_car_1.speed = 180
print(sport_car_1.name)
print(sport_car_1.color)
print(sport_car_1.speed)
sport_car_1.go()
sport_car_1.turn("налево")
sport_car_1.stop()

print('')

work_car_1 = WorkCar()
work_car_1.name = "Газель"
work_car_1.color = "Серый"
print(work_car_1.name)
print(work_car_1.color)
work_car_1.show_speed()
work_car_1.speed = 30
work_car_1.show_speed()

print('')

police_car_1 = PoliceCar()
print(police_car_1.is_police)
police_car_1.go()
police_car_1.turn("налево")
police_car_1.turn("направо")
police_car_1.stop()