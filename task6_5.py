from termcolor import colored


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Pen(Stationery):
    def draw(self):
        print("Текст " + colored(self.title, 'blue') + " отрисован ручкой.")


class Pencil(Stationery):
    def draw(self):
        print("Текст " + colored(self.title, 'grey') + " отрисован карандашом.")


class Handle(Stationery):
    def draw(self):
        print("Текст " + colored(self.title, 'red') + " отрисован маркером.")


title = input("Введите название предмета или нажмите Enter для завершения: ")
while title:
    Stationery(title).draw()
    while True:
        print("1 - для отрисовки карандашом\n"
              "2 - для отрисовки ручкой\n"
              "3 - для отрисовки маркером")
        choice = input()
        if choice == '1':
            Pencil(title).draw()
            break
        elif choice == '2':
            Pen(title).draw()
            break
        elif choice == '3':
            Handle(title).draw()
            break
        else:
            print("Нужно выбрать один из трех письменных принадлежностей. Попробуйте снова.")

    title = input("Введите текст или нажмите Enter для завершения: ")
