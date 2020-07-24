import json

with open("text_7.txt", "r", encoding="utf-8") as new_file:
    firm_list = []
    for string in new_file:
        firm_list.append(string.split())
    profit = []
    for i in range(len(firm_list)):
        firm_list[i].append(int(firm_list[i][2]) - int(firm_list[i][3]))
        if int(firm_list[i][2]) - int(firm_list[i][3]) >= 0:
            profit.append(int(firm_list[i][2]) - int(firm_list[i][3]))
    firms = [{firm_list[i][0]: firm_list[i][4] for i in range(len(firm_list))},
             {"average_profit": sum(profit) / len(profit)}]
    print(firms)
    with open("text_77.json", "w", encoding="utf-8") as new_file_2:
        json.dump(firms, new_file_2, indent=4)
