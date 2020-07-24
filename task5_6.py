with open("text_6.txt", "r", encoding="utf-8") as new_file:
    new_file_inf = new_file.read()
    new_file_strs = new_file_inf.split("\n")
    new_file_strs = (i.split(":") for i in new_file_strs)
    my_subject = dict(new_file_strs)
    for key, value in my_subject.items():
        new_value = 0
        for i in value.split():
            if i == "-":
                continue
            else:
                new_value += int(i[:i.find("(")])
        my_subject.update({key: new_value})
    print(my_subject)
