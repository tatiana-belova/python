import random

my_list = [random.randint(0, 100) for i in range(10)]
my_sum = 0
with open("text_5.txt", "w", encoding="utf-8") as new_file:
    for el in my_list:
        my_sum += el
        new_file.write(str(el) + " ")
print(f"Набор чисел {my_list} записан в файл text_5.txt\nСумма чисел в файле: {my_sum}")
