import numpy as np
import pandas as pd


def get_long(a_series, min_length=5):
    return a_series[a_series >= min_length]

data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
filtered = get_long(data)
print(data)
print(filtered)


"""
Длинные слова

Фильтрация данных — одна из первостепенных задач их анализа.

Напишите функцию get_long, принимающую серию формата первой задачи и фильтрующую её по именованному параметру min_length (по умолчанию 5).
Примечание

Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.
Пример 1
Ввод

data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
filtered = get_long(data)
print(data)
print(filtered)

Вывод

мир       3
питон     5
привет    6
яндекс    6
dtype: int64
питон     5
привет    6
яндекс    6
dtype: int64

Пример 2
Ввод

data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
filtered = get_long(data, min_length=6)
print(data)
print(filtered)

Вывод

мир       3
питон     5
привет    6
яндекс    6
dtype: int64
привет    6
яндекс    6
dtype: int64

"""