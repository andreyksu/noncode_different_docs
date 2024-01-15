# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

inputed = int(input())

order = 0
result = 0

target_num = inputed
while True:
    units = target_num % 10
    target_num = target_num // 10
    result = result * 10 + units
    if target_num < 10:
        result = result * 10 + target_num
        order += 1
        break
    else:
        order += 1

if order <= 1 or inputed != result:
    print("NO")
elif inputed == result:
    print("YES")
    

"""
А роза упала на лапу Азора 2.0
Вспомним о палиндромах, которые в обоих направлениях читаются одинаково. Напишите программу, которая проверяет, является ли число палиндромом.

Формат ввода
Одно натуральное число.

Формат вывода
YES — если число является палиндромом, иначе — NO.

Пример 1
    Ввод
        1234
    Вывод
        NO
Пример 2
    Ввод
        123454321
    Вывод
        YES
"""