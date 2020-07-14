my_list = [35, None, "lol", -89, 0.999, [1, 2, 3]]
n = 0
for i in range(int(len(my_list) / 2)):
    my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
    n += 2
print(my_list)
