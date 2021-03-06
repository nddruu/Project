# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self, height):
        mass = self._length * self._width * 25 * height / 1000
        return f"Необходимая масса асфальта: {mass:0.0f} т " \
               f"({self._length} м * {self._width} м * 25 кг * {height} см)"

r = road(int(input("Длина дороги (м): ")), int(input("Ширина дороги (м): ")))
print(r.mass_asphalt(int(input("Введите толщину дорожного полотна (см):"))))