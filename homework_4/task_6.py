#6. Реализовать два небольших скрипта:
#● итератор, генерирующий целые числа, начиная с указанного;
#● итератор, повторяющий элементы некоторого списка, определённого заранее.
#Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
#создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
#завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
#повторение элементов списка прекратится.

from itertools import count, cycle

st = int(input("Введите число с которого начинаем генерацию чисел: "))
my_list = []

for el in count(st):
    my_list.append(el)
    if len(my_list) > 14:
        break
print(f"Полученные числа: {my_list}")

my_tmpl = ["red", 123, False, [1, 2], {3, 4}, 3.14]
my_list = []

for el in cycle(my_tmpl):
    my_list.append(el)
    if len(my_list) > 14:
        break
print(f"Исходный список: {my_tmpl}")
print(f"Список сформированный их исходного: {my_list}")

#В качестве критерия выхода -- генерация 15 элементов
