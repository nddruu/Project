# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

#Создаем файл
my_list = [randint(1, 300) for n in range(1, 16)]
with open("text_5.txt", "w", encoding="utf-8") as my_f:
    print(*my_list, sep=" ", file=my_f)

#Считаем сумму чисел
with open("text_5.txt", "r", encoding="utf-8") as my_f:
    num_list = [int(n) for n in my_f.readline().split()]
    print("Сумма чисел: " + ", ".join(map(str,num_list)))
    print(f"Равна {sum(num_list)}")