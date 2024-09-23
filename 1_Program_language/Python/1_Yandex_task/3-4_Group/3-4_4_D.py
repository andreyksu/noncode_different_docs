from itertools import accumulate

inputed_str = input()

splited_str = inputed_str.split()
for i in range(len(splited_str)):
    splited_str[i] = splited_str[i] + " "

for accumulate_str in accumulate(splited_str):
    print(accumulate_str.strip())


"""
Словарная ёлка
Напишите программу, которая преобразует строку слов в ёлку как показано в примере.

Формат ввода
В одну строку через пробел вводятся слова разделенные пробелом.

Формат вывода
Несколько строк. В каждой следующей строке на одно слово больше.

Примечание
accumulate «складывает» не только числа.

Пример 1
Ввод
мама мыла раму
Вывод
мама
мама мыла
мама мыла раму

Пример 2
Ввод
картина корзина картонка
Вывод
картина
картина корзина
картина корзина картонка
"""