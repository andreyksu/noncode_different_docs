# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

current_hours = int(input())
currnet_minutes = int(input())
delta_in_nimute = int(input())

result_minutes = currnet_minutes + delta_in_nimute

delta_as_hours = result_minutes // 60
delta_as_ramains_minutes = result_minutes % 60

summ_of_hours = current_hours + delta_as_hours

result_hours = summ_of_hours % 24

# print(result_hours)
# print(delta_as_ramains_minutes)

print(f"{result_hours:02d}:{delta_as_ramains_minutes:02d}")

"""
В ожидании доставки
    Сегодня в N часов M минут хозяин магазина заказал доставку нового товара. Оператор сказал, что продукты доставят через T минут.
    Сколько будет времени на электронных часах, когда привезут долгожданные продукты?

Формат ввода
    В первой строке записано натуральное число N (0≤N<24).
    Во второй строке записано натуральное число M (0≤M<60).
    В третьей строке записано натуральное число T (30≤T<10^9).

Формат вывода
    Одна строка, представляющая циферблат электронных часов.
   
Пример 1
    Ввод
        8
        0
        65
    Вывод
        09:05
Пример 2
    Ввод
        10
        15
        2752
    Вывод
        08:07    
"""