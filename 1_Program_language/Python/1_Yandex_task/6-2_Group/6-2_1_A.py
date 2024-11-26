import numpy as np
import pandas as pd


def length_stats(raw_string):
    result_str = ""
    for i in raw_string:
        if i.isalpha() or i == " ":
            result_str = result_str + i
    result_str = result_str.lower()
    splited_str_as_list = result_str.split(" ")
    splited_str_as_list.sort()
    dict_of_string = {i: len(i) for i in splited_str_as_list if i != ""}
    s = pd.Series(dict_of_string)
    return s


print(length_stats("Мама мыла раму"))
print(length_stats("Лес, опушка, странный домик. Лес, опушка и зверушка."))
print(length_stats("Лес, опушка, странный домик. Лес, опушка и2 зверушка2."))
print(length_stats("Лес, опушка, странный домик. Лес, 2 опушка и2 зверушка2. dd"))

"""
Длины всех слов - 2
Напишите функцию length_stats, которая получает текст, а возвращает объект Series со словами в качестве индексов и их длинами в качестве значений.

Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(length_stats('Мама мыла раму'))
    Вывод
    мама    4
    мыла    4
    раму    4
    dtype: int64
Пример 2
Ввод
    print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
Вывод
    домик       5
    зверушка    8
    и           1
    лес         3
    опушка      6
    странный    8
    dtype: int64
"""