from time import sleep


class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 5}

    def running(self):
        follow = ("red", "yellow", "green", "yellow")
        while True:
            for i in follow:
                if i == "red":
                    print(f'\033[31m {i}')
                elif i == "yellow":
                    print(f'\033[33m {i}')
                elif i == "green":
                    print(f'\033[32m {i}')
                sleep(TrafficLight.__color.get(i))


light_1 = TrafficLight()
light_1.running()
