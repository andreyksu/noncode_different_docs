import numpy as np


def rotate(arrayy, corner):
    aN, aM = arrayy.shape

    countt = corner // 90

    for i in range(countt):
        arrayy = np.rot90(arrayy, -1)

    return arrayy


print(rotate(np.arange(12).reshape(3, 4), 90))
print(rotate(np.arange(12).reshape(3, 4), 270))


"""
Вращение
Напишите функцию rotate, принимающую двумерную матрицу и один из углов поворота: 
90
°
90°, 
180
°
180°, 
270
°
270° и 
360
°
360°.

Функция должна вернуть новую матрицу соответствующую заданному повороту по часовой стрелке.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(rotate(np.arange(12).reshape(3, 4), 90))
Вывод
    [[ 8  4  0]
    [ 9  5  1]
    [10  6  2]
    [11  7  3]]
Пример 2
Ввод
    print(rotate(np.arange(12).reshape(3, 4), 270))
Вывод
    [[ 3  7 11]
    [ 2  6 10]
    [ 1  5  9]
    [ 0  4  8]]
"""
