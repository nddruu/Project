#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
#платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
#время выполнения расчёта для конкретных значений необходимо запускать скрипт с
#параметрами.

from sys import argv

def my_args(args):
    try:
        script_name, output_in_hours, rate_per_hour, premium = args
        try:
            return dict(output_in_hours = float(output_in_hours), rate_per_hour = float(rate_per_hour),
                 premium = float(premium))
        except ValueError as err:
            return "Переданы не правильные параметры! Параметры должны быть числовыми!"
    except ValueError as err:
        if str(err).find("not enough values to unpack") != -1:
           return "Передано слишком мало параметров!"
        elif str(err).find("too many values to unpack") != 1:
            return "Передано слишком много параметров!"
        else:
            return "При выполнении произошла ошибка:" + str(err)


dict_param = my_args(argv)
if isinstance(dict_param, dict):
    salary = dict_param["output_in_hours"] * dict_param["rate_per_hour"] + dict_param["premium"]
    print(f"Зарплата сотрудника: {dict_param['output_in_hours']:0.2f} ч * {dict_param['rate_per_hour']:0.2f} руб + {dict_param['premium']:0.2f} руб = {salary:0.2f} руб")
else:
    print(dict_param)