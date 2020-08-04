class Equipment:
    def __init__(self, equipment_type, firm, model):
        self.equipment_type = equipment_type
        self.firm = firm
        self.model = model


class Printer(Equipment):
    def __init__(self, firm, model, type_printer, equipment_type="printer"):
        super().__init__(equipment_type, firm, model)
        self.type_printer = type_printer


class Scanner(Equipment):
    def __init__(self, firm, model, scan_method, equipment_type="scanner"):
        self.scan_method = scan_method
        super().__init__(equipment_type, firm, model)


class Copier(Equipment):
    def __init__(self, firm, model, copy_speed, equipment_type="copier"):
        self.copy_speed = copy_speed
        super().__init__(equipment_type, firm, model)


class My_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:
    def __init__(self):
        self.store = {"printer": [], "scanner": [], "copier": []}
        self.log = []

    def in_store(self, type_id, firm, model, num, feature):
        if type_id == 1:
            a = Printer(firm, model, feature)
        elif type_id == 2:
            a = Scanner(firm, model, feature)
        elif type_id == 3:
            a = Copier(firm, model, feature)

        list_equipment = self.store.get(a.equipment_type)
        new = True
        try:
            for i in list_equipment:
                if i.get("firm") == a.firm and i.get("model") == a.model:
                    new = False
                    i.update({"num": i.get("num") + int(num)})
        except ValueError:
            self.log.append("Error! При поступлении на склад указано не верное значение количества оборудования!")
        else:
            self.log.append(f"Поступление на склад: {a.equipment_type} {firm} {model} в кол-ве {num} шт.")
        if new:
            if type_id == 1:
                list_equipment.append({"firm": a.firm, "model": a.model, "type_printer": a.type_printer, "num": num})
            elif type_id == 2:
                list_equipment.append({"firm": a.firm, "model": a.model, "type_printer": a.scan_method, "num": num})
            elif type_id == 3:
                list_equipment.append({"firm": a.firm, "model": a.model, "type_printer": a.copy_speed, "num": num})

    def out_store(self, type_id, firm, model, num, to):
        if type_id == 1:
            __a = "printer"
            list_equipment = self.store.get(__a)
        elif type_id == 2:
            __a = "scanner"
            list_equipment = self.store.get(__a)
        elif type_id == 3:
            __a = "copier"
            list_equipment = self.store.get(__a)

        try:
            for i in list_equipment:
                if i.get("firm") == firm and i.get("model") == model:
                    if i.get("num") < num:
                        raise My_Error("Внимание! На складе недостаточно оборудования!")
                    else:
                        self.log.append(f"Перемещение со склада в {to}: {__a} {firm} {model} в кол-ве {num} шт.")
                        i.update({"num": i.get("num") - num})
        except My_Error as err:
            self.log.append(f"Попытка перемещения со склада в {to}: {__a} {firm} {model} в кол-ве {num} шт.")
            self.log.append(f"{err}")


my_store = Store()
my_store.in_store(1, "Brother", "HL", 10, "лазерный")
my_store.in_store(1, "Pantum", "P2207", "десять", "лазерный")
my_store.in_store(1, "Canon", "TS704", 5, "струйный")
my_store.in_store(2, "Epson", "122", 12, "линейный")
my_store.in_store(2, "CanoScan", "LiDE 300", 3, "линейный")
my_store.in_store(3, "Xerox", "002", 25, 100)
my_store.in_store(3, "Xerox", "KFT-789", 7, 100)
my_store.out_store(1, "Canon", "V1", 11, "Бухгалтерия")
my_store.out_store(3, "Xerox", "X1000", 15, "ПТО")
print(my_store.store)
print("\n".join(str(my_store.log).split(',')))
