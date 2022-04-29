# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

from random import randint

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = randint(0, speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = randint(5, 80)
        return f"Машина поехала со скоростью {self.speed}"

    def stop(self):
        self.speed = 0
        return "Машина остановилась"

    def turn(self, direction):
        return f"Машина повернула на {direction}"

    def show_speed(self):
        self.speed = randint(5, 80)
        return f"Машина едет со скоростью {self.speed}"

    def info_car(self):
        return f"Данные машины \nИмя: {self.name} \nЦвет: {self.color} \nСкорость: {self.speed}" \
               f"\nОсобые отметки: {'Полицейский автомобиль' if self.is_police else 'Нет'}"

class TownCar(Car):

    def show_speed(self):
        loc = super().show_speed()
        if self.speed > 60:
            loc += "\n\033[31mОбнаружено превышение скорости!\033[0m"
        return loc

class SportCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)
        self.speed = speed #Стартуем сразу на максимальной скорости, мы же спортивные

class WorkCar(Car):

    def show_speed(self):
        loc = super().show_speed()
        if self.speed > 40:
            loc += "\n\033[31mОбнаружено превышение скорости!\033[0m"
        return loc

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

# print("Городская машина")
# tc = TownCar(60, "Зелененькая", "Ласточка")
# print(tc.info_car())
# print(tc.turn("лево"))
# print(tc.stop())
# print(tc.speed)

# print("Спортивная машина")
# sc = SportCar(150, "Красненькая", "Быстпвя Ласточка")
# print(sc.info_car())
# sc.name = "Мятая ласточка (не справилась с управлением)"
# sc.speed = 20
# print(sc.info_car())

# print("Служебная машина")
# wc = WorkCar(100, "Чорная", "Очэнь крутой машина")
# print(wc.info_car())
# print(wc.show_speed())

print("Полицейская машина")
pc = PoliceCar(200, "Стандартная раскраска", "Скользит как тигр, жалит как пчела")
print(pc.info_car())
