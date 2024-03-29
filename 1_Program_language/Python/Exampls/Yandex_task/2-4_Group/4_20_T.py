# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

target_num = int(input())

target = 0
summ = 0

for i in range(10, 2, -1):
    tmpp = target_num
    tmpp_summ = 0
    while True:
        remainder = tmpp % i
        tmpp = tmpp // i
        # print(f"remainder = {remainder}, tmpp = {tmpp}, i = {i}")
        if tmpp >= i:
            tmpp_summ = tmpp_summ + remainder
            continue
        else:
            tmpp_summ = tmpp_summ + remainder + tmpp
            break
    # print(f"tmpp_summ = {tmpp_summ}")
    if tmpp_summ >= summ:
        target = i
        summ = tmpp_summ

print(target)

"""
Математическая выгода
Математик Виталий Евгеньевич задумался над вопросом выгоды систем счисления. Он решил, что выгодной системой счисления будет являться та, в которой число имеет наибольшую сумму цифр. Напишите программу, которая по введённому числу определяет основание системы счисления с максимальной выгодой.

Формат ввода
Одно натурально число.

Формат вывода
Одно натуральное число из диапазона [2;10] — основание системы счисления с максимальной выгодой.
Если таких оснований несколько, выбирается наименьшее.

Примечание
Подробнее о системах счисления можно почитать здесь

Пример 1
    Ввод
    12
    Вывод
    7
Пример 2
    Ввод
    52
    Вывод
    9
"""
