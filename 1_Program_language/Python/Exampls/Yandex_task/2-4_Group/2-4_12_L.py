# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

first_side = int(input())
second_side = int(input())

dimension = first_side * second_side

width = 0
a = dimension
while a > 0:
    width += 1
    a = a // 10

# print(width)


target_numm = 0

for i in range(1, first_side + 1):
    for j in range(1, second_side + 1):
        target_numm += 1
        print(f"{target_numm:>{width}}", end=" ")
    print()

"""
Числовой прямоугольник
Ребята в детском саду учатся считать, и чтобы им было интереснее, воспитательница решила оформить список изучаемых чисел особым образом.
Дети справляются весьма быстро, поэтому ей требуется программа способная строить числовые прямоугольники. Напишите программу, которая строит числовой прямоугольник требуемого размера.

Формат ввода
В первой строке записано число N — высота числового прямоугольника.
Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода
Нужно вывести сформированный числовой прямоугольник требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец должен быть одинаковой ширины.

Пример 1
    Ввод
        2
        3
    Вывод
1 2 3
4 5 6
Пример 2
    Ввод
        4
        6
    Вывод
 1  2  3  4  5  6
 7  8  9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
"""