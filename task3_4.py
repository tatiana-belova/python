"""возведение в степень с помощью оператора **"""
def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(int(input("Введите число x: ")), int(input("Введите число y: "))))
"""реализация без оператора **, предусматривающая использование цикла."""
def my_func(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x
print(my_func(int(input("Введите число x: ")), int(input("Введите число y: "))))