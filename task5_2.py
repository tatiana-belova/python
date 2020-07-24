try:
    with open("text_2.txt", "r", encoding="utf-8") as new_file:
        strings = [line.rstrip() for line in new_file.readlines()]
        print(f"Количество строк в файле - {len(strings)}.")
        for i in range(len(strings)):
            print(f"Количество слов в строке №{i + 1} - {len(strings[i].split())}.")
except IOError:
    print("Файла не существует.")