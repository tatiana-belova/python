class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-": my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f"Дата верна"
                else:
                    return f"Неверный формат года"
            else:
                return f"Неверный формат месяца"
        else:
            return f"Неверный формат числа"

    def __str__(self):
        return f"Текущая дата {Data.extract(self.day_month_year)}"


today = Data("4 - 8 - 2020")
print(today)
print(Data.valid(25, 12, 1997))
print(today.valid(89, 12, 2011))
print(today.valid(9, 13, 2011))
print(today.valid(9, 12, 2101))
print(Data.extract("29 - 03 - 1996"))
print(today.extract("19 - 07 - 2020"))
print(Data.valid(1, 11, 2000))
