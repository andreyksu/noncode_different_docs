# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

first = int(input())
second = int(input())
third = int(input())

first_digits = first % 10
first_units = first // 10

second_digits = second % 10
second_units = second // 10

third_digits = third % 10
third_units = third // 10

if first_digits == second_digits == third_digits:
    print(first_digits)
elif first_units == second_units == third_units:
    print(first_units)
else:
    print("NO")

"""
Властелин Чисел: Братство общей цифры
Во времена магии и драконов существовало мнение, что числа обладают великой силой, способной изменить мир.

Всё началось с написания великих чисел. Три числа были переданы эльфам. Семь — отданы повелителям гномов. А девять... были переданы человеческому роду.

Но все они оказались обмануты, потому что существовало ещё одно число. В стране Нумия на бумаге из тёмного папируса властелин Зерон тайно написал Единую Цифру, подчиняющую себе все великие числа.

Давайте выясним, что это за цифра.

Формат ввода
В первой строке записано двузначное число одного из эльфов.
Во второй строке — Гномов.
В третьей — Людей.

Формат вывода
Одна цифра — общая у всех трёх чисел в одинаковой позиции

Пример 1
    Ввод
        12
        13
        14
    Вывод
        1

Пример 2
    Ввод
        23
        13
        63
    Вывод
        3
"""