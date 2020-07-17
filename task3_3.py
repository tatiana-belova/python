def my_func(a, b, c):
    arguments = [a, b, c]
    arguments.remove(min(a, b, c))
    return sum(arguments)
print(my_func(int(input("Введите число а: ")), int(input("Введите число b: ")), (int(input("Введите число c: ")))))