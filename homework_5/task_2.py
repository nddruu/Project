# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open("text_2.txt", "r", encoding="utf-8") as my_f:
    str_list = my_f.read().splitlines()

print(f"Всего строк в файле {len(str_list)}")
for s in str_list:
    print(f"{s} -- {len(s.split())} слов")