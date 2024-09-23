# Это решение прошедшее проверки. Но решение не является верным с точки зрения алгоритма в части польской обратной записи. 
# В алгоритме используется стек как промежуточная сущность.

# Задача решена с учётом порядка подачи материала (методов/функций, еще не было. По коллекциям дали только что list). Решал так если бы не знал методы итд.
inputed_str = input()

list_of_binar_oper = ["+", "-", "*", "/"]
list_of_unar_oper = ["~", "!", "#"]
list_of_ternar_oper = ["@"]

in_str_as_list = inputed_str.split()

fuzze = True
i = 0
while fuzze:
    result = None
    current_item = in_str_as_list[i]
    if current_item in list_of_binar_oper:
        first = int(in_str_as_list[i - 2])
        second = int(in_str_as_list[i - 1])
        operation = in_str_as_list[i]
        if operation == "*":
            result = first * second
        elif operation == "/":
            result = first // second
        elif operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        tmp_list = in_str_as_list[: i - 2]
        tmp_list.append(result)
        in_str_as_list = tmp_list + in_str_as_list[i + 1 :]
        i = 0
    elif current_item in list_of_unar_oper:
        first = int(in_str_as_list[i - 1])
        operation = in_str_as_list[i]
        if operation == "~":
            first = first * (-1)
            in_str_as_list[i - 1] = first
            in_str_as_list = in_str_as_list[:i] + in_str_as_list[i + 1 :]
        elif operation == "!":
            first = int(in_str_as_list[i - 1])
            kk = 1
            result = 1
            while kk <= first:
                result = result * kk
                kk += 1
            in_str_as_list[i - 1] = result
            in_str_as_list = in_str_as_list[:i] + in_str_as_list[i + 1 :]
        elif operation == "#":
            first = int(in_str_as_list[i - 1])
            in_str_as_list[i] = first
        i = 0
    elif current_item in list_of_ternar_oper:
        first = int(in_str_as_list[i - 3])
        second = int(in_str_as_list[i - 2])
        third = int(in_str_as_list[i - 1])
        in_str_as_list[i - 3] = second
        in_str_as_list[i - 2] = third
        in_str_as_list[i - 1] = first
        in_str_as_list = in_str_as_list[:i] + in_str_as_list[i + 1 :]
        i = 0
    else:
        i += 1
    if len(in_str_as_list) <= 1:
        break

print(in_str_as_list[0])

"""
Польский калькулятор — 2
Потренируемся в ОПН дальше. Операции, которые выполняются с одним значением, называются унарными, с двумя — бинарными, с тремя — тернарными. Давайте улучшим наш калькулятор, добавив поддержку следующих операций:

бинарные:
+ (сложение),
- (вычитание),
* (умножение),
/ (деление нацело; для отрицательных чисел работает по тем же правилам, что и в Python);
унарные:
~ (унарный минус — меняет знак),
! (факториал),
# (клонирование — вернуть в стек значение дважды);
тернарные:
@ (возвращает в стек те же три значения, но в ином порядке: второе, третье, первое).
Формат ввода
Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций. Вместе они составляют корректное выражение в обратной польской нотации, не содержащее деления на ноль и взятия факториала от отрицательного числа.

Формат вывода
Выводится одно целое число — результат вычисления выражения.

Примечание
В первом примере стек по мере прочтения строки выглядит так:

7
7 1
7 1 10
7 1 10 100
7 1 10 100 100
7 1 10 10000
7 10 10000 1
7 10 9999
7 10009
10016
-10016

Пример 1
    Ввод
    7 1 10 100 # * @ - + + ~
    Вывод
    -10016

Пример 2
    Ввод
    10 15 - 7 *
    Вывод
    -35
"""
