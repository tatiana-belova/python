from googletrans import Translator

translator = Translator()

with open("text_4.txt", "r", encoding="utf-8") as start_file:
    with open("text_4.1.txt", "w", encoding="utf-8") as new_file:
        lines = [line.rstrip() for line in start_file.readlines()]
        for line in lines:
            result = translator.translate(line, src="en", dest="ru")
            new_file.write(result.text + "\n")