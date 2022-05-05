# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class NoEquipFromStockEx(Exception):
    def __init__(self, st, eq, current, need):
        self.st = st
        self.eq = eq
        self.current = current
        self.need = need

    def __str__(self):
        return f"На складе '{self.st.name}' не хватает '{self.eq.name}' есть {self.current} шт из {self.need}"

class Stock:

    def __init__(self, name):
        self.name = name
        self.__storage = {}

    #Информация о хранимой на складе оргтехнике
    def storage_info(self):
        print(f"Содержимое склада {self.name}")
        print("\n".join([f"{n}: Доступно {self.__storage[n]} шт" for n in self.__storage.keys()]))

    #Поступление оргтехники
    def append(self, office_equip, quant):
        self.__storage[office_equip] = self.__storage[office_equip] + quant if office_equip in self.__storage else quant

    #Выбытие оргтехники
    def leaving(self, office_equip, quant):
        if not office_equip in self.__storage or self.__storage[office_equip] < quant:
            raise NoEquipFromStockEx(self, office_equip, self.__storage[office_equip] if office_equip in self.__storage else 0,quant)
        else:
            self.__storage[office_equip] = self.__storage[office_equip] - quant if office_equip in self.__storage else - quant

    #Перемещение орг техники
    def transfer(self, other_stock, office_equip, quant):
        self.leaving(office_equip, quant)
        other_stock.append(office_equip, quant)

class OfficeEquip:

    def __init__(self, name, articul, vendor):
        self.name = name
        self.articul = articul
        self.vendor = vendor

class Printer(OfficeEquip):

    def __init__(self, name, articul, vendor, type):
        super().__init__(name, articul, vendor)
        self.type = type    #Laser|Led|Inkjet|Matrix

    def __str__(self):
        return f"Принтер {self.name} (Артикул {self.articul}; Производитель {self.vendor}; Тип {self.type})"

class Scanner(OfficeEquip):

    def __init__(self, name, articul, vendor, dpi):
        super().__init__(name, articul, vendor)
        self.dpi = dpi

    def __str__(self):
        return f"Сканер {self.name} (Артикул {self.articul}; Производитель {self.vendor}; Разрешение {self.dpi})"

class Copy(OfficeEquip):

    def __init__(self, name, articul, vendor, speed):
        super().__init__(name, articul, vendor)
        self.speed = speed

    def __str__(self):
        return f"Копировальный аппарат {self.name} (Артикул {self.articul}; Производитель {self.vendor}; Скорость {self.speed})"

p_1 = Printer("HP LasepJet", "HPLJ-0124", "HP", "Laser")
p_2 = Printer("ECOSYS P2335d", "KES-0012", "Kyocera", "Laser")
s_1 = Scanner("CanoScan LiDE 400", "CAN-0512", "Canon", "600")
s_2 = Scanner("Epson Perfection V19", "EPS-0452", "Epson", "600")
c_1 = Copy("Canon FC108", "CAN-0516", "Canon", "7")

st_1 = Stock("Основной склад")
st_2 = Stock("Бухгалтерия")

#Приходуем оборудование на основной склад
st_1.append(p_1, 2)
st_1.append(p_1, 5)
st_1.append(p_2, 1)
st_1.append(s_1, 5)
st_1.append(s_2, 2)
st_1.append(c_1, 1)

# Перемещаем
try:
    st_1.transfer(st_2, p_1, 5)
except NoEquipFromStockEx as err:
    print(err)

try:
    st_1.transfer(s_2, c_1, 5)
except NoEquipFromStockEx as err:
    print(err)

# Выбытие
try:
    st_2.leaving(s_1, 3)
except NoEquipFromStockEx as err:
    print(err)

# Смотрим что на складах
st_1.storage_info()
st_2.storage_info()
