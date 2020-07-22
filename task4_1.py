from sys import argv

script_name, work_hours, rate, bonus = argv
wage = (int(work_hours) * int(rate)) + int(bonus)
print(f"Заработная плата: {wage}")