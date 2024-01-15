class Rectangle:
    def __init__(self, aRec_1, aRec_2):
        self.rec_1 = aRec_1
        self.rec_2 = aRec_2

    def __getLenght(self):
        return round(abs(self.rec_1[0] - self.rec_2[0]), 2)

    def __getHeight(self):
        return round(abs(self.rec_1[1] - self.rec_2[1]), 2)

    def get_pos(self):
        left_upper_x = round(min(self.rec_1[0], self.rec_2[0]), 2)
        left_upper_y = round(max(self.rec_1[1], self.rec_2[1]), 2)
        return (left_upper_x, left_upper_y)

    def get_size(self):
        return (self.__getLenght(), self.__getHeight())

    def move(self, dx, dy):
        self.rec_1 = (self.rec_1[0] + dx, self.rec_1[1] + dy)
        self.rec_2 = (self.rec_2[0] + dx, self.rec_2[1] + dy)

    def resize(self, width, height):
        pos = self.get_pos()
        x1 = pos[0]
        y1 = pos[1] - height

        x2 = pos[0] + width
        y2 = pos[1]

        self.rec_1 = (x1, y1)
        self.rec_2 = (x2, y2)

    def perimeter(self):
        return round(self.__getLenght() * 2 + self.__getHeight() * 2, 2)

    def area(self):
        return round(self.__getLenght() * self.__getHeight(), 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())

"""
Классный прямоугольник 2.0
Расширим функционал класса написанного вами в предыдущей задаче.

Реализуйте методы:

get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
get_size() — возвращает размеры в виде кортежа;
move(dx, dy) — изменяет положение на заданные значения;
resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.
Все результаты вычислений нужно округлить до сотых.

Пример 1
Ввод
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
Вывод
(3.2, 3.14) (4.32, 7.44)
(4.52, -1.86) (4.32, 7.44)

Пример 2
Ввод
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
Вывод
(3.2, 3.14) (4.32, 7.44)
(3.2, 3.14) (23.5, 11.3)
"""