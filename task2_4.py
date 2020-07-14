new_string = input("Введите строку: ")
n = new_string.split(" ")
for i, el in enumerate(n, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}) {el}")
