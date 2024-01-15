# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

# ### - Означает(требуется оптимизация) - решение не очень нравится
# Переосмыслить - не очень нравится решение
first_side = int(input())
second_side = int(input())

target_num = 0

dimension = first_side * second_side

width = 0
a = dimension
while a > 0:
    width += 1
    a = a // 10

target = 0

for i in range(1, first_side + 1):
    for j in range(1, second_side + 1):
        if j == 1:
            target = i * j
            print(f"{target:>{width}}", end=" ")
        elif j % 2 == 0:
            target = (first_side * j) - (i - 1)
            print(f"{target:>{width}}", end=" ")
        else:
            target = (first_side * (j-1)) + i
            print(f"{target:>{width}}", end=" ")
    print()


"""
Числовая змейка 2.0
Воспитательнице вновь нужна программа, которая будет генерировать змейку из чисел. Напишите программу, которая строит числовую змейку требуемого размера.

Формат ввода
В первой строке записано число N — высота числового прямоугольника.
Во второй строке указано число M — ширина числового прямоугольника.

Формат вывода
Нужно вывести сформированную числовую змейку требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.

Пример 1
    Ввод
        2
        3
    Вывод
        1 4 5
        2 3 6
Пример 2
    Ввод
        4
        6
    Вывод
        1  8  9 16 17 24
        2  7 10 15 18 23
        3  6 11 14 19 22
        4  5 12 13 20 21
"""