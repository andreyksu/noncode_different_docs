# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

first_side = int(input())
second_side = int(input())

target_num = 0

dimension = first_side * second_side

width = 0
a = dimension
while a > 0:
    width += 1
    a = a // 10

for i in range(1, first_side + 1):
    for j in range(0, second_side):
        target_num = i + (first_side * j)
        # print(target_num, end=" ")
        print(f"{target_num:>{width}}", end=" ")
    print()

"""
Числовой прямоугольник 2.0
Давайте вновь поможем воспитательнице учить ребят числам. Напишите программу, которая строит числовой прямоугольник требуемого размера.

Формат ввода
В первой строке записано число N — высота числового прямоугольника.
Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода
Нужно вывести сформированный числовой прямоугольник требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец должен обладать одинаковой шириной.

Пример 1
    Ввод
        2
        3
    Вывод
1 3 5
2 4 6

Пример 2
    Ввод
        4
        6
    Вывод
 1  5  9 13 17 21
 2  6 10 14 18 22
 3  7 11 15 19 23
 4  8 12 16 20 24
"""