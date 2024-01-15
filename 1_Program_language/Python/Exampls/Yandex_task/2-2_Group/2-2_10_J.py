# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

input_digital = int(input())

hundreds = input_digital // 100
tens = (input_digital % 100) // 10
units = input_digital % 10

first_summ = tens + units
second_summ = hundreds + tens

if first_summ > second_summ:
    print(f"{first_summ}{second_summ}")
else:
    print(f"{second_summ}{first_summ}")

"""
Лучшая защита — шифрование
Коля испугался, что Аня подсмотрит все его пароли в блокноте, и решил их зашифровать. Для этого он берёт изначальный пароль — трёхзначное число — и по нему строит новое число по следующим правилам:

находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы);
находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
Эти две суммы, записанные друг за другом, в порядке не возрастания, формируют новое число.
Помогите реализовать алгоритм шифрования.

Формат ввода
Одно трёхзначное число

Формат вывода
Результат шифрования

Пример 1
    Ввод
        123
    Вывод
        53
Пример 2
    Ввод
        741
    Вывод
        115
"""