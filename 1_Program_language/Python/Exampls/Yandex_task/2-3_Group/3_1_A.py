# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

target_str = "Три!"
strr = ""
count = 0
while True:
    strr = input()
    if target_str in strr:
        break
    else:
        count += 1
        continue

for i in range(0, count):
    print("Режим ожидания...")
else:
    print("Ёлочка, гори!")


"""
Раз, два, три! Ёлочка, гори!
В детском саду проводят новогодний утренник. Со знанием чисел и их порядком у детей пока есть небольшие проблемы, но цифру три знают все без исключения.

Напишите программу, которая зажигает Ёлочку, когда все дети прокричат «Три!»

Формат ввода
    Вводятся крики детей.

Формат вывода
    Выводить «Режим ожидания...», пока дети не прокричат «Три!».
    В конце вывести «Ёлочка, гори!»

Пример 1
    Ввод
        Раз!
        Два!
        Три!
    Вывод
        Режим ожидания...
        Режим ожидания...
        Ёлочка, гори!
Пример 2
    Ввод
        Десять!
        Девять!
        Раз!
        Три!
    Вывод
        Режим ожидания...
        Режим ожидания...
        Режим ожидания...
        Ёлочка, гори!
"""