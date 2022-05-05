# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой

class NotDivZeroEx(Exception):

    def __str__(self):
        return "Делить на ноль нельзя!!!"

class Division:

    @staticmethod
    def Check(d_2):
        if d_2 == 0:
            raise NotDivZeroEx

d_1 = int(input("Введите делимое: "))
d_2 = int(input("Введите делитель: "))
try:
    Division.Check(d_2)
    print(f"{d_1} / {d_2} = {d_1 / d_2:0.2f}")
except NotDivZeroEx as err:
    print(err)