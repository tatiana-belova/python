def int_func(word):
    return word.title()


while True:
    words = input("Введите слова из маленьких латинских букв. Слова разделите пробелами: ")
    words_list = words.split()
    res = ''
    num = 0
    for word in words_list:
        for letter in word:
            if ord(letter) > 122 or ord(letter) < 97:
                print(f"Недопустимые символы. Введите слова, состоящие ТОЛЬКО из маленьких латинских букв. Слова разделите пробелами: ")
                num += 1
                break
        if num > 0:
            continue
        else:
            res += int_func(word) + ' '
    if num == 0:
        print(f"Исходная строка, но каждое слово начинается с заглавной буквы: {res}")
        break
