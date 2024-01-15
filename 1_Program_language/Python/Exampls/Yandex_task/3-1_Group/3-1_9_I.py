# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.

listt = list()
str_for_search = "#"

tmp_str = ""
while (target_str := input()) != "":
    position_of_sharp = target_str.find(str_for_search)
    if position_of_sharp == 0:
        pass
    elif position_of_sharp == -1:
        listt.append(target_str)
    else:
        tmp_str = target_str[: position_of_sharp]
        listt.append(tmp_str)

for i in listt:
    print(i)


"""
Без комментариев
Мы надеемся, вы пишите комментарии к своему коду. Если так, то интерпретатор удаляет их перед тем, как выполнить код. Напишите программу, которая выполняет данную функцию за интерпретатор.

Формат ввода
Вводятся строки программы.
Признаком остановки является пустая строка.

Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не надо.

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