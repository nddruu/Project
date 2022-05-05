# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class Compl:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return f"{self.r} {'+' if self.i > 0 else '-'} {abs(self.i)}i"

    def __add__(self, other):
        return Compl(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Compl(self.r * other.r - self.i * other.i, self.r * other.i + other.r * self.i)

c_1 = Compl(15, 1.5)
c_2 = Compl(1.1, -12)
print(f"({c_1}) + ({c_2}) = {c_1 + c_2}")
print(f"({c_1}) * ({c_2}) = {c_1 * c_2}")
