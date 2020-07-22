def fact(num: int):
    if num <= 0:
        yield 1

    result = 1

    for el in range(1, num + 1):
        result *= el
        yield result


def my_fact(num: int):
    for el in fact(num):
        print(el)


my_fact(int(input("Введите число: ")))
