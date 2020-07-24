with open("text_3.txt", "r", encoding="utf-8") as new_file:
    employees = [line.rstrip() for line in new_file.readlines()]
    surnames = ""
    wages = 0
for i in range(len(employees)):
    employee = employees[i].split()
    wage = float(employee[1])
    wages += wage
    if wage < 20000:
        surnames += employee[0] + " "
print(f"Средняя величина дохода сотрудников: {round(wages / len(employees), 3)}")
print(f"Сотрудники, имеющие оклад менее 20 тыс: {surnames}")
