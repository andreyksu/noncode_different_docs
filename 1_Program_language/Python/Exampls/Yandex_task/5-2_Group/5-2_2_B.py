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
point.move(2, -3)
print(repr(point))
# ----------------------------
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))

"""
Классная точка 4.0
А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические методы _str__ и _repr__.

При преобразовании в строку точка представляется в формате (x, y).
Репрезентация же должна возвращать строку для инициализации точки двумя параметрами.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    point = PatchedPoint()
    print(point)
    point.move(2, -3)
    print(repr(point))
Вывод
    (0, 0)
    PatchedPoint(2, -3)
Пример 2
Ввод
    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    print(*map(str, (first_point, second_point)))
    print(*map(repr, (first_point, second_point)))
Вывод
    (2, -7) (7, 9)
    PatchedPoint(2, -7) PatchedPoint(7, 9)
"""