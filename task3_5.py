def my_func():
    func_result = 0
    _exit = False
    while _exit == False:
        num = input("Введите числа через пробел или q, чтобы выйти: ").lower().split()
        result = 0
        for el in range(len(num)):
            if num[el] == 'q':
                _exit = True
                break
            else:
                result = result + int(num[el])
        func_result = func_result + result
        print(f"Сумма всех чисел, введённых вами на данный момент: {func_result}")
    print(f"Сумма всех введённых чисел: {func_result}")


my_func()
