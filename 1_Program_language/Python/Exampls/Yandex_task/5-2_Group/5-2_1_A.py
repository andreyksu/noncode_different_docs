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
            
class PatchedPoint1(Point):
    def __init__(self, a_x=None, a_y=None):
        if a_x is None and a_y is None:
            super().__init__(0, 0)
        elif isinstance(a_x, tuple):
            super().__init__(a_x[0], a_x[1])
        else:
            super().__init__(a_x, a_y)

point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
print("--------")
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
print("======================================")
point = PatchedPoint1()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
print("--------")
first_point = PatchedPoint1((2, -7))
second_point = PatchedPoint1(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
print("======================================")