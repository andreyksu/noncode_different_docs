# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

input_num = int(input())

hundreds = input_num // 100
tens = (input_num % 100) // 10
units = input_num % 10

min_dig = min(hundreds, tens, units)
max_dig = max(hundreds, tens, units)

summ = hundreds + tens + units
medium_num = summ - (min_dig + max_dig)

# if hundreds != min_dig and hundreds != max_dig: # ошибка на 112 и 221 для medium см. 2_11_task.py 
#    medium_num = hundreds
# elif tens != min_dig and tens != max_dig:
#    medium_num = tens
# else:
#    medium_num = units
    
# print (f"max_dig = {max_dig}     medium_num = {medium_num}      min_dig = {min_dig}")

max_pair = str(max_dig) + str(medium_num) # А можно просто домножением на 10 и сложение.

if min_dig == 0:
    min_pair = str(medium_num) + str(min_dig)
else:
    min_pair = str(min_dig) + str(medium_num)

print(f"{min_pair} {max_pair}")

"""
Властелин Чисел: Две Башни
Во времена, когда люди верили в великую силу чисел, оказалось, что волшебник Пифуман предал все народы и стал помогать Зерону.

Чтобы посетить башни обоих злодеев одновременно, нам следует разделить магию числа, которое защищало нас в дороге.

Чтобы поделить трёхзначное число, нам нужно составить из него минимально и максимально возможные двухзначные числа.

Формат ввода
    Одно трёхзначное число.

Формат вывода
    Два защитных числа для каждого отряда, записанные через пробел.

Пример 1
    Ввод
        103
    Вывод
        10 31
Пример 2
    Ввод
        787
    Вывод
        77 87
"""
