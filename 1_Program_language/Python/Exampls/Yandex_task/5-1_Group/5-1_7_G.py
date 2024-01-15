"""
Здесь работа ведётся относительно центра и длин сторон.
Это решение прошло все тесты.

Удивительно. что по проверкам, что располагаются ниже, результат один в один. Значит проверка где-то в другом проявляется.
"""


class Rectangle:
    def __init__(self, aRec_1, aRec_2):
        self.center = self.get_center(aRec_1, aRec_2)
        self.lenght = self.__getLenght(aRec_1, aRec_2)
        self.height = self.__getHeight(aRec_1, aRec_2)

    def __getLenght(self, firstPoitn, secondPoitn):
        len = abs(firstPoitn[0] - secondPoitn[0]) + 0.0
        return round(len, 2)

    def __getHeight(self, firstPoint, secondPoint):
        height = abs(firstPoint[1] - secondPoint[1]) + 0.0
        return round(height, 2)

    def get_center(self, firstPoint, secondPoint):
        x_center = round((firstPoint[0] + secondPoint[0]) / 2, 2)
        y_center = round((firstPoint[1] + secondPoint[1]) / 2, 2)
        return (x_center, y_center)

    def getCenter(self):
        return self.center

    # Левый верхний угол
    def get_left_upper_point(self):
        left_upper_x = round(self.center[0] - self.lenght / 2, 2)
        left_upper_y = round(self.center[1] + self.height / 2, 2)
        return (left_upper_x, left_upper_y)

    def get_right_bottom_point(self):
        left_upper_x = round(self.center[0] + self.lenght / 2, 2)
        left_upper_y = round(self.center[1] - self.height / 2, 2)
        return (left_upper_x, left_upper_y)

    def get_pos(self):
        return self.get_left_upper_point()

    def get_size(self):
        return (self.lenght, self.height)

    def move(self, dx, dy):
        tmp_x = self.center[0] + dx
        tmp_y = self.center[1] + dy
        self.center = (tmp_x, tmp_y)

    def resize(self, new_width, new_height):
        self.lenght = round(new_width, 2)
        self.height = round(new_height, 2)

    def perimeter(self):
        return round((self.lenght * 2 + self.height * 2), 2)

    def area(self):
        return round((self.lenght * self.height), 2)

    def turn(self):
        self.lenght, self.height = self.height, self.lenght

    def scale(self, factor):
        self.lenght = round(self.lenght * factor, 2)
        self.height = round(self.height * factor, 2)


print("G-2_" * 5)
"""
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep=" ")
rect.turn()
print(rect.get_pos(), rect.get_size(), sep=" ")
rect.turn()
print(rect.get_pos(), rect.get_size(), sep=" ")
rect.turn()
print(rect.get_pos(), rect.get_size(), sep=" ")
rect.turn()
print(rect.get_pos(), rect.get_size(), sep=" ")


print("\n\n\n")

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep=" ")
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep=" ")
rect.scale(0.5)

print(rect.get_pos(), rect.get_size(), sep=" ")
rect.scale(0.5)
print(rect.get_pos(), rect.get_size(), sep=" ")
rect.scale(2)
print(rect.get_pos(), rect.get_size(), sep=" ")
"""

# print("\n\n\n")
rect = Rectangle((2, 5), (4, 1))
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.scale(2.0)
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.scale(2.0)
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.move(1, 1)
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.move(-1, -1)
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.scale(0.5)
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.scale(0.5)
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
print("-" * 100)
rect = Rectangle((2, -1), (4, -5))
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
print("-" * 100)
rect = Rectangle((-4, -5), (-2, -1))
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
print("-" * 100)
rect = Rectangle((-4, 5), (-2, 1))
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
print("-" * 100)
rect = Rectangle((-2, 1), (2, -1))
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
print("-" * 100)
rect = Rectangle((-1, 2), (1, -2))
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
rect.turn()
print(
    rect.get_pos(),
    rect.get_right_bottom_point(),
    rect.getCenter(),
    rect.get_size(),
    sep=" ",
)
print("-" * 100)
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep="\t")
rect.turn()
print(rect.get_pos(), rect.get_size(), sep="\t")

print("-" * 100)
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep="\t")
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep="\t")

print("-" * 100)
rect = Rectangle((-6, -3), (-2, -7))
print(rect.get_pos(), rect.get_size(), rect.getCenter(), sep="\t")
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), rect.getCenter(), sep="\t")

"""
Классный прямоугольник 3.0
Необходимо ещё немного доработать предыдущую задачу.

Разработайте методы:

turn() — поворачивает прямоугольник на 90&deg; по часовой стрелке вокруг его центра;
scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
Все вычисления производить с округлением до сотых.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
Вывод
(-3.14, 2.71)
(6.28, 5.42)
(-2.71, 3.14)
(5.42, 6.28)

Пример 2
Ввод
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')
Вывод
(-3.14, 2.71)
(6.28, 5.42)
(-6.28, 5.42)
(12.56, 10.84)
"""
