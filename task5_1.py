with open("text_1.txt", "w", encoding="utf-8") as new_file:
    print("Введите данные построчно. Если ввод закончен, оставьте пустую строку и нажмите Enter.")
    while True:
        strings = input()
        if strings == "":
            break
        else:
            new_file.write(strings + "\n")