import numpy as np


def snake(aM, aN, direction="H"):
    aa = np.zeros((aN, aM), dtype="int16")
    if direction == "H":
        targetCount = 1
        for i in range(1, aN + 1):
            tmpListt = list()
            if i % 2 != 0:
                for ii in range(targetCount, (aM * i) + 1):
                    tmpListt.append(ii)
                else:
                    targetCount = ii
            if i % 2 == 0:
                for ii in range(aM * i, targetCount, -1):
                    tmpListt.append(ii)
                else:
                    targetCount = aM * i + 1
            a = np.asarray(tmpListt)
            aa[i - 1] = a
    if direction == "V":
        for i in range(1, aN + 1):
            tmpListt = list()
            for ii in range(1, aM + 1):
                if ii % 2 != 0:
                    tmpListt.append((ii - 1) * aN + i)
                else:
                    tmpListt.append(ii * aN - (i - 1))
            a = np.asarray(tmpListt)
            aa[i - 1] = a

    return aa


print(snake(5, 3))
print(snake(5, 3, direction="V"))
"""
Числовая змейка 3.0
Когда-то вы помогали детсадовцам с различными змейками. Давайте реализуем её на основе массивов.

Напишите функцию snake, которая принимает ширину (
𝑀
M) и высоту (
𝑁
N) змейки, а также именованный параметр direction.

Параметр direction могут принимать значения:

H — горизонтальная змейка, используется по умолчанию;
V — вертикальная змейка.
Функция должна вернуть матрицу, представляющую змейку, с ячейками типа int16.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(snake(5, 3))
Вывод
    [[ 1  2  3  4  5]
    [10  9  8  7  6]
    [11 12 13 14 15]]
Пример 2
Ввод
    print(snake(5, 3, direction='V'))
Вывод
    [[ 1  6  7 12 13]
    [ 2  5  8 11 14]
    [ 3  4  9 10 15]]
"""
