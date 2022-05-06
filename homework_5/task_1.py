# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

str_list = []
while True:
    str_in_f = input("Введите строку для добавления в файл (для окончания пустой ввод):")
    if str_in_f == "":
        break
    str_list.append(str_in_f + "\n")
if len(str_list) == 0:
    print("Файл не создан! Нет данных для ввода!")
else:
    with open("task_1_data.txt", "w", encoding="utf-8") as my_f:
        my_f.writelines(str_list)