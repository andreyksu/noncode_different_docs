class Rectangle:
    def __init__(self, aRec_1, aRec_2):
        self.rec_1 = aRec_1
        self.rec_2 = aRec_2

    def __getLenght(self):
        # print(abs(self.rec_1[0] - self.rec_2[0]))
        return abs(self.rec_1[0] - self.rec_2[0])

    def __getHeight(self):
        # print(abs(self.rec_1[1] - self.rec_2[1]))
        return abs(self.rec_1[1] - self.rec_2[1])

    def perimeter(self):
        return round(self.__getLenght() * 2 + self.__getHeight() * 2, 2)

    def area(self):
        return round(self.__getLenght() * self.__getHeight(), 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())

'''
Внимание. Здесь может быть указана координата любого угла. Т.е. и нижняя левая или правая и верхняя левая или правая в любом порядке (просто говорится, что они диагональные.)
'''

"""
Классный прямоугольник
Давайте перейдём к более сложным геометрическим фигурам.

Разработайте класс Rectangle.

При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника (со сторонами параллельными осям координат).

Класс должен реализовывать методы:

perimeter — возвращает периметр прямоугольника;
area — возвращает площадь прямоугольника.
Все результаты вычислений нужно округлить до сотых.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
Вывод
23.52

Пример 2
Ввод
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
Вывод
32.14
"""