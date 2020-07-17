def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name = input("Ведите ваше имя: "), surname = input("Ведите вашу фамилию: "), year = input("Ведите год вашего рождения: "), city = input("Ведите город проживания: "), email = input("Ведите адрес вашей электронной почты: "), telephone = input("Ведите ваш номер телефона: ")))
