#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
#деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
#ноль.

def my_division(dividend, divider):
    try:
        dividend, divider = float(dividend), float(divider)
    except ValueError as err:
        return "Не верные значения делимого или делителя. Будьте мнимательнее!"
    try:
        return dividend / divider
    except ZeroDivisionError as err:
        return "Делитель не можкт быть равным 0!"

print(my_division(input("Введите делимое: "), input("Введите делитель: ")))
