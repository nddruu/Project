#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
#платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
#время выполнения расчёта для конкретных значений необходимо запускать скрипт с
#параметрами.

from sys import argv

script_name, output_in_hours, rate_per_hour, premium = argv

salary = int(output_in_hours) * int(rate_per_hour) + int(premium)

print(f"Зарплата сотрудника: {output_in_hours} ч * {rate_per_hour} руб + {premium} руб = {salary} руб")