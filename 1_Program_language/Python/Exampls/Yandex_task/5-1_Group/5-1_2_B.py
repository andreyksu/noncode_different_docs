class Point:
    def __init__(self, a_x, a_y):
        self.x = a_x
        self.y = a_y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, a_point):
        return round(
            ((self.x - a_point.x) ** 2 + (self.y - a_point.y) ** 2) ** (0.5), 2
        )


point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))

"""
Классная точка 2.0
Давайте расширим функционал класса, написанного в прошлой задаче.

Реализуйте методы:

move, который перемещает точку на заданное расстояние по осям x и y;
length, который определяет до переданной точки расстояние, округлённое до сотых.
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    point = Point(3, 5)
    print(point.x, point.y)
    point.move(2, -3)
    print(point.x, point.y)
Вывод
    3 5
    5 2
Пример 2
Ввод
    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))
Вывод
    16.76
    16.76
"""