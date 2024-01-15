class Point:
    def __init__(self, a_x, a_y):
        self.x = a_x
        self.y = a_y
        
point = Point(3, 5)
print(point.x, point.y)

point = Point(2, -7)
print(point.x, point.y)

"""
Классная точка
Объектно-ориентированное программирование — популярная парадигма в современном мире. Это вполне очевидно, ведь любой объект реального мира мы теперь можем представить в виде цифрового набора полей и методов. Давайте приступим к проектированию классов.

Разработайте класс Point, который при инициализации принимает координаты точки на декартовой плоскости и сохраняет их в поля x и y соответственно.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    point = Point(3, 5)
    print(point.x, point.y)
Вывод
    3 5
Пример 2
Ввод
    point = Point(2, -7)
    print(point.x, point.y)
Вывод
    2 -7
"""