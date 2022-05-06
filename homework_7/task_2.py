# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

from abc import ABC, abstractmethod

class  Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_consumption(self):
        pass

    def __str__(self):
        return f"Одежда {self.name}"

class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def tissue_consumption(self):
        return f"Расход ткани: {(self.size/6.5 + 0.5):0.2f}"


class Suit(Clothes):

    def __init__(self, name, length ):
        super().__init__(name)
        self.length = length

    @property
    def tissue_consumption(self):
        return f"Расход ткани: {(self.length * 2 + 0.3):0.2f}"

сoat = Coat("Пальто", 50)
print(f"{сoat};  {сoat.tissue_consumption}")

suit = Suit("Костюм", 185)
print(f"{suit};  {suit.tissue_consumption}")
