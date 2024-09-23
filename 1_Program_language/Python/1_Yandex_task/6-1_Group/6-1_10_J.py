import numpy as np


def stairs(arrayy):
    aN = arrayy.size
    aa = np.zeros((aN, aN), dtype="int16")
    aa[0] = arrayy
    for i in range(1, aN):
        firstPart = arrayy[:-1]
        lastPart = arrayy[-1:]
        arrayy = np.append(lastPart, firstPart)
        aa[i] = np.append(lastPart, firstPart)
    return aa


print(stairs(np.arange(3)))
print(stairs(np.arange(5)))


"""
Лесенка
Напишите функцию stairs, принимающую вектор и возвращающую матрицу, в которой каждая строка является копией вектора со смещением.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(stairs(np.arange(3)))
Вывод
    [[0 1 2]
    [2 0 1]
    [1 2 0]]
Пример 2
Ввод
    print(stairs(np.arange(5)))
Вывод
    [[0 1 2 3 4]
    [4 0 1 2 3]
    [3 4 0 1 2]
    [2 3 4 0 1]
    [1 2 3 4 0]]
"""