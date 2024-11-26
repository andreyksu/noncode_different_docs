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


class PatchedPoint(Point):
    def __init__(self, a_x=None, a_y=None):
        if a_x is None and a_y is None:
            Point.__init__(self, 0, 0)
        elif isinstance(a_x, tuple):
            Point.__init__(self, a_x[0], a_x[1])
        else:
            Point.__init__(self, a_x, a_y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        tmpX = self.x + other[0]
        tmpY = self.y + other[1]
        return PatchedPoint(tmpX, tmpY)

    def __radd__(self, other):
        tmpX = self.x + other[0]
        tmpY = self.y + other[1]
        return PatchedPoint(tmpX, tmpY)

    def __iadd__(self, other):
        self.x = self.x + other[0]
        self.y = self.y + other[1]
        return self


class PatchedPoint1(Point):
    def __init__(self, a_x=None, a_y=None):
        if a_x is None and a_y is None:
            super().__init__(0, 0)
        elif isinstance(a_x, tuple):
            super().__init__(a_x[0], a_x[1])
        else:
            super().__init__(a_x, a_y)


point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)
# --------------------------------------------------
print("-" * 50)
# --------------------------------------------------
first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)

"""
Классная точка 5.0
Согласитесь, что использовать операторы куда удобнее, чем обыкновенные методы. Давайте вспомним о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.

При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной на заданное кортежем расстояние по осям x и y.
При выполнении кода point += (x, y) производится перемещение изначальной точки.

Напомним, что сейчас мы модернизируем только класс PatchedPoint.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    point = PatchedPoint()
    print(point)
    new_point = point + (2, -3)
    print(point, new_point, point is new_point)
Вывод
    (0, 0)
    (0, 0) (2, -3) False

Пример 2
Ввод
    first_point = second_point = PatchedPoint((2, -7))
    first_point += (7, 3)
    print(first_point, second_point, first_point is second_point)
Вывод
    (9, -4) (9, -4) True
"""