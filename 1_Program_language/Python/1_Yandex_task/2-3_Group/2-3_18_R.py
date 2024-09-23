# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

target_number = int(input())

result_str = ""
target = int(target_number**0.5)

is_simple = True
if target_number <= 3:
    pass
else:
    for i in range(2, target + 1):
        if target_number % i == 0:
            is_simple = False
            while target_number % i == 0:
                target_number = int(target_number / i)
                if result_str == "":
                    result_str = result_str + str(i)
                else:
                    result_str = result_str + " * " + str(i)
        else:
            continue
    else:
        # Исключаем для простых числе вывод в виде "* target_num" а для составных в конце "* 1"
        if target_number != 1 and not is_simple:
            result_str = result_str + " * " + str(target_number)

print(result_str)

"""
Простая задача 2.0
В банке решили переписать программу для шифрования данных и попросили, чтобы вы взяли на себя часть данной задачи. Напишите программу для разложения числа на простые множители. 
Только внимательно, ведь работать придётся вновь с простыми числами.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется составить математическое выражение — произведение простых неубывающих чисел, которое в результате даёт исходное.

Пример 1
    Ввод
        120
    Вывод
        2 * 2 * 2 * 3 * 5
Пример 2
    Ввод
        98
    Вывод
        2 * 7 * 7
"""
