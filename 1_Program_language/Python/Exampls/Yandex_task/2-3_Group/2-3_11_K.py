# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

num = int(input())
summ = 0
tmp = 0

if num < 10:
    summ = num
else:
    while num >= 10:
        unit = num % 10
        summ = summ + unit
        num = num // 10
    else:
        summ = summ + num

print(summ)


"""
Цифровая сумма
Иногда требуется манипулировать с цифрами чисел.
Одно из самых простых действий, которое можно совершить — найти сумму цифр числа. Напишите программу, чтобы выполнить это действие.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется вывести одно натуральное число — сумму цифр исходного.

Пример 1
    Ввод
        12345
    Вывод
        15
Пример 2
    Ввод
        100500
    Вывод
        6
"""
