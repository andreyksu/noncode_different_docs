# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

name = input()
mood = input()

print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
if mood == "хорошо":
    print("Я за вас рада!")
elif mood == "плохо":
    print("Всё наладится!")

"""
Просто здравствуй, просто как дела
    Умение вести диалог — важный навык для воспитанного человека.
    Напишите диалоговую программу, которая сначала познакомится с пользователем, а затем поинтересуется его настроением.

Формат ввода
    В первой строке записано имя пользователя.
    Во второй — ответ на вопрос: «хорошо» или «плохо».

Формат вывода
    В первой строке должен быть вопрос «Как Вас зовут?»
    Во второй строке — «Здравствуйте, %username%!»
    В третьей строке — вопрос «Как дела?»
    В четвёртой строке реакция на ответ пользователя:

        если пользователь ответил «хорошо», следует вывести сообщение «Я за вас рада!»;
        если пользователь ответил «плохо», следует вывести сообщение «Всё наладится!».
Пример 1
    Ввод
        Аня
        хорошо
    Вывод
        Как Вас зовут?
        Здравствуйте, Аня!
        Как дела?
        Я за вас рада!
"""