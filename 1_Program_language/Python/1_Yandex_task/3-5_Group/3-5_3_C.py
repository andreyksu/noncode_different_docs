from sys import stdin

listt = list()

for line in stdin:
    tmp_str = line.rstrip("\n")
    if "#" in tmp_str:
        position = tmp_str.index("#")
        tmp_str = tmp_str[:position].rstrip()
    if len(tmp_str) == 0:
        continue
    listt.append(tmp_str)

for i in listt:
    print(i)


"""
Без комментариев 2.0
Как вы помните, когда вы комментируете свой код, перед его выполнением интерпретатор удаляет комментарии.
Напишите программу, которая выполняет данную функцию за интерпретатор.

Формат ввода
Вводятся строки программы.

Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не нужно.

Пример 1
Ввод
# Моя первая супер-пупер программа
print("What is your name?") #  Как тебя зовут?
name = input() #  Сохраняем имя
print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы
Вывод
print("What is your name?")
name = input()
print(f"Hello, {name}!")


Пример 2
Ввод
# Мой первый цикл
for i in range(10): # Считаем до 10
    print(i) # выводим число
Вывод
for i in range(10):
    print(i)
"""