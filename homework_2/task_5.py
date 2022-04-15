#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
#не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
#существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
#должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввёл число 3. Результат: 7, 5, 3, 3, _3_, 2.
#Пользователь ввёл число 8. Результат: _8_, 7, 5, 3, 3, 2.
#Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, _1_.
#Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(f"Начальный рейтинг {my_list}")
while True:
    new = int(input("Введите натуральное число: "))
    tmp_list = []
    while len(my_list) != 0 and new > my_list[-1]:
        tmp_list.insert(0, my_list.pop())
    my_list.append(new)
    my_list.extend(tmp_list)
    print(f"Новый рейтинг {my_list}")
    if input("Продолжить (y/n): ") != "y":
        break