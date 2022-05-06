#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
#возвращает сумму наибольших двух аргументов

def my_func(first, second, third):
    try:
        first, second, third = int(first), int(second), int(third)
    except ValueError as err:
        return "Вы ошиблись при вводе чисел, числа должны быть целыми!"
    min_num = min([first, second, third])
    max_list = list(filter(lambda x: x != min_num, [first, second, third]))
    if len(max_list) == 2:
        return sum(max_list)
    elif len(max_list) == 1:
        #Граничный случай: например [11, 11, 12] два одинаковых минимальных элемента
        return max_list[0] + min_num
    else:
        #Граничный случай: передано три одинаковых элемента
        return min_num + min_num

print("Сложение наибольших двух чисел из трех")
print(my_func(input("Введите первое число: "),
              input("Введите второе число: "),
              input("Введите третье число: ")))