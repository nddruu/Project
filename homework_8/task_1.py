# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class NotMonthOrYearEx(Exception):

    def __init__(self, month = 0, year = 0):
        self.month = month
        self.year = year

    def __str__(self):
        if self.month != 0 and self.year == 0:
            return f"Ошибка в указании месяца {self.month}"
        elif self.month == 0 and self.year != 0:
            return f"Ошибка в указании года {self.year}"
        elif self.month != 0 and self.year != 0:
            return f"Ошибка в указании месяца {self.month} и года {self.year}"

class Data:

    def __init__(self, days, month, year):
        self.days = days
        self.month = month
        self.year = year

    def __str__(self):
        return ".".join(map(str,[self.days, self.month, self.year]))

    @classmethod
    def transform(cls, strdata):
        list_data = [int(n) for n in strdata.split("-")]
        cls.check(list_data[1], list_data[2])
        return Data(list_data[0], list_data[1], list_data[2])

    @staticmethod
    def check(month, year):
        if month < 1 or month > 12 or year < 1900:
            raise NotMonthOrYearEx(month if month < 1 or month > 12 else 0,
                                   year if year < 1900 else 0)

while True:
    strd = input("Введите дату в формате ДД-ММ-ГГГГ: ")
    if strd == "":
        break
    try:
        data = Data.transform(strd)
        print(data)
    except NotMonthOrYearEx as err:
        print(err)
