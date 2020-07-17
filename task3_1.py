def my_func (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
print(my_func(int(input("Введите число а: ")), int(input("Введите число b: "))))


