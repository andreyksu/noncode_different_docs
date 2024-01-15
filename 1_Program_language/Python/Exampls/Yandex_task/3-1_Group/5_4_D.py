# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.

listt = list()

prefix = "##"
postfix = "@@@"

while (strr := input()) != "":
    if strr.endswith(postfix):
        continue
    while strr.startswith(prefix):
        strr = strr[2:]
    listt.append(strr)
    
for i in listt:
    print(i)
    
"""
Очистка данных
Местный провайдер собирает большое количество логов, однако зачастую файлы с отчётами приходят в негодность.
Самые частые проблемы — ошибки вида ## и @@@.
Напишите программу, которая избавляется от:

Двух символов # в начале информационных сообщений;
Строк, заканчивающихся тремя символами @.
Формат ввода
Вводятся строки отчёта. Признаком завершения ввода считается пустая строка.

Формат вывода
Очищенные данные.

Пример 1
    Ввод
    Hello, world
    Hello, @@@
    ##Goodbye

    Вывод
    Hello, world
    Goodbye
Пример 2
    Ввод
    First Message
    ##Second Message
    @@@Third Message##
    ##Fourth Message@@@

    Вывод
    First Message
    Second Message
    @@@Third Message##
"""