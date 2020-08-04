class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


def value_exception(num):
    try:
        complex(num)
        return 0
    except ValueError:
        return 1


num_list = []
print("Для завершения ввода оставьте пустую строку и нажмите Enter.")
while True:
    try:
        el = input("Введите число: ")
        if el == '':
            break
        elif not value_exception(el):
            num_list.append(el)
        else:
            raise MyError("Элемент не является числом!")
    except MyError as err:
        print(err)

print(f"Ваш список: {num_list}")
