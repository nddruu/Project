#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

numstr = input("Введите произвольное число: ")
print(f"{numstr} + {numstr + numstr} + {numstr + numstr + numstr} = {int(numstr) + int(numstr + numstr) + int(numstr + numstr + numstr)}")