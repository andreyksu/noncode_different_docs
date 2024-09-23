"""
Здесь работа ведётся относительно 2х координат. Верхний левый угол и правый нижний.

"""


class Rectangle:
    def __init__(self, aRec_1, aRec_2):
        self.set_points(aRec_1, aRec_2)
        left_upper_corner = self.get_left_upper_point()
        right_bottom_corner = self.get_right_bottom_point()
        self.set_points(left_upper_corner, right_bottom_corner)

    def set_points(self, aRec_1, aRec_2):
        self.rec_1 = aRec_1
        self.rec_2 = aRec_2

    def __getLenght(self):
        return abs(self.rec_1[0] - self.rec_2[0]) + 0.0

    def __getHeight(self):
        return abs(self.rec_1[1] - self.rec_2[1]) + 0.0

    # Левый верхний угол
    def get_left_upper_point(self):
        left_upper_x = round(min(self.rec_1[0], self.rec_2[0]), 2) + 0.0
        left_upper_y = round(max(self.rec_1[1], self.rec_2[1]), 2) + 0.0
        return (left_upper_x, left_upper_y)

    # Правый нижний угол
    def get_right_bottom_point(self):
        right_bottom_x = round(max(self.rec_1[0], self.rec_2[0]), 2) + 0.0
        right_bottom_y = round(min(self.rec_1[1], self.rec_2[1]), 2) + 0.0
        return (right_bottom_x, right_bottom_y)

    def get_pos(self):
        return self.get_left_upper_point()

    def get_size(self):
        return (round(self.__getLenght(), 2), round(self.__getHeight(), 2))

    def move(self, dx, dy):
        self.rec_1 = (round(self.rec_1[0] + dx, 2), round(self.rec_1[1] + dy, 2))
        self.rec_2 = (round(self.rec_2[0] + dx, 2), round(self.rec_2[1] + dy, 2))

    def resize(self, new_width, new_height):
        left_upper_point = self.get_left_upper_point()

        x1 = left_upper_point[0]
        y1 = left_upper_point[1]

        x2 = left_upper_point[0] + new_width
        y2 = left_upper_point[1] - new_height

        self.set_points((x1, y1), (x2, y2))

    def perimeter(self):
        return round((self.__getLenght() * 2 + self.__getHeight() * 2), 2)

    def area(self):
        return round((self.__getLenght() * self.__getHeight()), 2)

    def getCenter(self):
        lenght = self.__getLenght()
        height = self.__getHeight()
        tmpp_x, tmpp_y = self.get_pos()
        x_center = round(tmpp_x + lenght / 2, 2)
        y_center = round(tmpp_y - height / 2, 2)
        return (x_center, y_center)

    def turn(self):
        half_lenght = round(self.__getLenght() / 2, 2)
        half_height = round(self.__getHeight() / 2, 2)

        center = self.getCenter()

        tmp1 = (center[0] - half_height, center[1] + half_lenght)
        tmp2 = (center[0] + half_height, center[1] - half_lenght)

        self.set_points(tmp1, tmp2)

    def scale(self, factor):
        half_lenght = round(self.__getLenght() / 2, 2)
        half_height = round(self.__getHeight() / 2, 2)

        scaled_half_lenght = round(half_lenght * factor, 2)
        scaled_half_height = round(half_height * factor, 2)

        center = self.getCenter()

        self.rec_1 = (center[0] - scaled_half_lenght, center[1] + scaled_half_height)
        self.rec_2 = (center[0] + scaled_half_lenght, center[1] - scaled_half_height)


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

print("G-3_" * 5)
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
