# -----------------------------------------
# src_list = [input() for a in range(2)]
# int_list = [int(a.split("=")[-1].strip()) for a in src_list]
# x = [y**2 for y in range(int_list[0], int_list[1] + 1)]
# print(x)
# -----------------------------------------
# print([y**2 for y in range(int(input().split("=")[-1].strip()), int(input().split("=")[-1].strip()) + 1)])
# -----------------------------------------
[y**2 for y in range(int(a), int(b) + 1)]


"""
Список квадратов
Большинство задач этой главы ориентированы на отработку навыков по построению списочных выражений.

Вашему решению будет предоставлены две переменные a и b. Напишите списочное выражение для получения квадратов чисел из диапазона [a,b].

Примечание
В решении не должно быть ничего, кроме списочного выражения.

Пример 1
Ввод
a = 1
b = 5
Вывод
[1, 4, 9, 16, 25]

Пример 2
Ввод
a = -5
b = 5
Вывод
[25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
"""