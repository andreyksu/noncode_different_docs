import numpy as np
import pandas as pd


def length_stats(a_raw_string):
    evenStr = ""
    oddStr = ""

    fullList = a_raw_string.split(".")

    for i, strr in enumerate(fullList):
        if i % 2 == 0:
            evenStr = evenStr + " " + strr
        else:
            oddStr = oddStr + " " + strr

    def length_stats_inner(raw_string):
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

    return (length_stats_inner(oddStr), length_stats_inner(evenStr))


odd, even = length_stats('Мама мыла раму')
print(odd)
print(even)

odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(odd)
print(even)

"""
# Решение не подходит. Т.к. здесь чередуются по чётности и нечётности предложения а не длина слов.
# Так то оно работает, но не по условия. Не стал удалять.

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
