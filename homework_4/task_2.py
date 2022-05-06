#2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
#которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его
#формирования используйте генератор.
#Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#Результат: [12, 44, 4, 10, 78, 123].

from random import randint

print("----Вариант с заданным списком----")
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[n] for n in range(1, len(my_list)) if my_list[n] > my_list[n - 1]]
print(f"Исходный список: {my_list}")
print(f"Список с условием: {new_list}")

print("----Вариант со случайным списком----")
my_list = [randint(1, 300) for n in range(1, 16)]
new_list = [my_list[n] for n in range(1, len(my_list)) if my_list[n] > my_list[n - 1]]
print(f"Исходный список: {my_list}")
print(f"Список с условием: {new_list}")
