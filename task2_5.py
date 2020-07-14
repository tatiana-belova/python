my_list = [8, 6, 4, 2, 0]
number = int(input("Введите новый элемент рейтинга: "))
n = my_list.count(number)
for element in my_list:
    if n > 0:
        i = my_list.index(number)
        my_list.insert(i + n, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
