# Задача решена с учётом порядка подачи материала (методов итд, еще не было). Решал так если бы не знал перечисленного.

inputed_str = input()
str_as_set = set(inputed_str)
# print(str_as_set)
result_str = "".join(str_as_set)
print(result_str)


"""
Символическая выжимка
Во многих промышленных задачах требуется понимать, из каких символов состоят данные. Напишите программу, чтобы по введённой строке она определяла, из каких символов та состоит.

Формат ввода
Вводится одна строка.

Формат вывода
Требуется вывести все символы этой строки без повторений.
Порядок вывода не имеет значения.

Пример 1
    Ввод
    змееед
    Вывод
    здме

Пример 2
    Ввод
    велосипед
    Вывод
    исолвдеп
"""