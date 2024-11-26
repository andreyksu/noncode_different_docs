class Rectangle:
    def __init__(self, aRec_1, aRec_2):
        self.set_corner1(aRec_1, aRec_2)

    def set_corner(self, aRec_1, aRec_2):
        if aRec_1[0] < aRec_2[0]:
            self.rec_1 = aRec_1
            self.rec_2 = aRec_2
        else:
            self.rec_1 = aRec_2
            self.rec_2 = aRec_1
            
    def set_corner1(self, aRec_1, aRec_2):
        self.rec_1 = aRec_1
        self.rec_2 = aRec_2
        
    # +++
    def __getLenght(self):
        return abs(self.rec_1[0] - self.rec_2[0])

    # +++
    def __getHeight(self):
        return abs(self.rec_1[1] - self.rec_2[1])

    # +++
    def get_pos(self):
        left_upper_x = round(min(self.rec_1[0], self.rec_2[0]), 2)
        left_upper_y = round(max(self.rec_1[1], self.rec_2[1]), 2)
        return (left_upper_x, left_upper_y)

    # +++
    def get_size(self):
        return (round(self.__getLenght(), 2), round(self.__getHeight(), 2))

    def move(self, dx, dy):
        self.rec_1 = (round(self.rec_1[0] + dx, 2), round(self.rec_1[1] + dy, 2))
        self.rec_2 = (round(self.rec_2[0] + dx, 2), round(self.rec_2[1] + dy, 2))

    def resize(self, new_width, new_height):
        pos = self.get_pos()
        x1 = pos[0]
        y1 = pos[1] - new_height

        x2 = pos[0] + new_width
        y2 = pos[1]

        self.rec_1 = (x1, y1)
        self.rec_2 = (x2, y2)

    def perimeter(self):
        return round(self.__getLenght() * 2 + self.__getHeight() * 2, 2)

    def area(self):
        return round(self.__getLenght() * self.__getHeight(), 2)

    def __getCenter(self):
        lenght = self.__getLenght()
        height = self.__getHeight()
        tmpp_x, tmpp_y = self.get_pos()
        #x_center = round(self.rec_1[0] + lenght / 2, 2)
        #y_center = round(self.rec_1[1] + height / 2, 2) # А почему здесь плюс??? Может здесь нужно вычитать т.к. это может быть угол левый вердхний.
        x_center = round(tmpp_x + lenght / 2, 2)
        y_center = round(tmpp_y - height / 2, 2)
        return (x_center, y_center)

    def turn(self):
        half_lenght = round(self.__getLenght() / 2, 2)
        half_height = round(self.__getHeight() / 2, 2)

        center = self.__getCenter()

        tmp1 = (center[0] - half_height, center[1] - half_lenght)
        tmp2 = (center[0] + half_height, center[1] + half_lenght)

        self.set_corner(tmp1, tmp2)

    def scale(self, factor):
        if factor == 0:
            factor = 1
        half_lenght = round(self.__getLenght() / 2, 2)
        half_height = round(self.__getHeight() / 2, 2)

        scaled_half_lenght = round(half_lenght * factor, 2)
        scaled_half_height = round(half_height * factor, 2)

        center = self.__getCenter()

        self.rec_1 = (center[0] - scaled_half_lenght, center[1] - scaled_half_height)
        self.rec_2 = (center[0] + scaled_half_lenght, center[1] + scaled_half_height)


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
