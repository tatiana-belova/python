things = []
while input("Добавить новый товар в список? Ответьте: да/нет: ") == "да":
    num = int(input("Введите номер товара: "))
    property = {}
    while input("Добавить характеристики товара? Ответьте: да/нет: : ") == "да":
        property_key = input("Введите параметр товара: ")
        property_value = input("Введите значение параметра товара: ")
        property[property_key] = property_value
    things.append(tuple([num, property]))
print(things)

analisys = {}
for thing in things:
    for property_key, property_value in thing[1].items():
        if property_key in analisys:
            analisys[property_key].append(property_value)
        else:
            analisys[property_key] = [property_value]
print(analisys)
