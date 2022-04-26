# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

# with open("text_7.txt", "r", encoding="utf-8") as my_txt:
#     profit = {st.split()[0]: int(st.split()[2]) - int(st.split()[3]) for st in my_txt}
#
# positive = [int(n) for n in profit.values() if int(n) > 0]
#
# with open("text_7_json.txt", "w", encoding="utf-8") as my_json:
#     json.dump([profit, {"all_profit": round(sum(positive) / len(positive))}], my_json, ensure_ascii=False, indent=4)

#Подсократил
with open("text_7_json.txt", "w", encoding="utf-8") as my_json:
    with open("text_7.txt", "r", encoding="utf-8") as my_txt:
        profit = {st.split()[0]: int(st.split()[2]) - int(st.split()[3]) for st in my_txt}
        positive = [int(n) for n in profit.values() if int(n) > 0]
        json.dump([profit, {"all_profit": round(sum(positive) / len(positive))}], my_json, ensure_ascii=False, indent=4)