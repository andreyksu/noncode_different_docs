# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

child_count = int(input())

result = 0

for i in range(0, child_count):
    numm = int(input())
    tmpp = numm
    tmp_max = 0
    while tmpp > 0:
        units = tmpp % 10
        tmpp = tmpp // 10
        if tmp_max < units:
            tmp_max = units
            # print(f"tmp_max = {tmp_max} units = {units}")
    factor = 1 if i > 0 else 0
    result = (result * 10 * factor) + tmp_max

print(result)


"""
Большое число
Дети никак не успокоятся и продолжают «мучить» числа. Сейчас они хотят общими силами составить очень большое число. Каждый ребёнок называет число состоящее из цифр, которые он знает. Напишите программу, которая строит число, состоящее из максимальных цифр каждого ребёнка.

Формат ввода
В первой строке указано число N — количество детей в группе. В каждой из последующих N строк записано число.

Формат вывода
Одно большое число.

Пример 1
    Ввод
        2
        123
        234
    Вывод
        34
Пример 2
    Ввод
        3
        1234
        7234
        2323
    Вывод
        473
"""