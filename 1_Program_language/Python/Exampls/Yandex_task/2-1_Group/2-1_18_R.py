# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

purcchase_cost = input()
banknote = int(input())

purcase_cost_as_int = int(purcchase_cost, 2)

change = banknote - purcase_cost_as_int

print(change)

"""
Сдача 10
    Кстати, несмотря на ошибку аппарата, сдачу тоже нужно отдавать.

Формат ввода
    Цена покупки — двоичное число, выданное кассовым аппаратом.
    Номинал купюры пользователя — десятичное число (≥100).

Формат вывода
    Одно десятичное число — сдача, которую требуется отдать пользователю.

Примечание
    Все числа, используемые в задаче, целые.

Пример 1
    Ввод
        1001001
        100
    Вывод
        27
Пример 2
    Ввод
        101111100
        500
    Вывод
        120
"""