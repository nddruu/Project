#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
#Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
#разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
#добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
#этих чисел к полученной ранее сумме и после этого завершить программу.

def my_summ(str_num, sum_all):
    """Возвращает список со следующими значениями
        index_0 - Сумма из переданной строки
        index_1 - Сумма общая
        index_2 - Были ли в переданной строке ошибки (True/False)
        index_3 - Был ли передан символ завершения (True/False)
    """
    sum_loc = 0
    str_list = str_num.split()
    err = False
    q = False
    for e in str_list:
        if e == "q" or e == "Q":
            q = True
        else:
            try:
                sum_loc += int(e)
            except ValueError as err_:
                err = True

    return [sum_loc, sum_all + sum_loc, err, q]

s = 0
err = "Err\n"
emp = ""
while True:
    res_l = my_summ(input("Введите строку с числами через пробел: "), s)
    print(f"{err if res_l[2] else emp}{res_l[0]}({res_l[1]})")
    if res_l[3]:
        break
    s = res_l[1]