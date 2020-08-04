class Zero_Division_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_division(num_1, num_2):
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        if num_2 == 0:
            raise Zero_Division_Error("На ноль делить нельзя!")
    except Zero_Division_Error as err:
        return err
    except ValueError:
        return "Вводить можно только числа!"
    else:
        return round(num_1 / num_2, 2)


a, b = (input("Введите делимое: "), input("Введите делитель: "))
print(my_division(a, b))