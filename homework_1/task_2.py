#2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

total = int(input("Введите количество секунд: "))
ss = total % 60
total = total // 60
mm = total % 60
total = total // 60
print(f"Форматированное время: {total:02}:{mm:02}:{ss:02}")