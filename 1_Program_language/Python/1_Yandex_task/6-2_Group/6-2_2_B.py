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
    odd = s[s % 2 != 0]
    even = s[s % 2 == 0]
    return (odd, even)


odd, even = length_stats("Мама мыла раму")
print(odd)
print(even)

odd, even = length_stats("Лес, опушка, странный домик. Лес, опушка и зверушка.")
print(odd)
print(even)

"""
Длины всех слов по чётности
В этот раз продумайте функцию length_stats, которая получает текст, а возвращает пару объектов Series со словами в качестве индексов и их длинами в качестве значений.

Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    odd, even = length_stats('Мама мыла раму')
    print(odd)
    print(even)
Вывод
    Series([], dtype: int64)
    мама    4
    мыла    4
    раму    4
    dtype: int64
Пример 2
Ввод
    odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
    print(odd)
    print(even)
Вывод
    домик    5
    и        1
    лес      3
    dtype: int64
    зверушка    8
    опушка      6
    странный    8
    dtype: int64
"""
