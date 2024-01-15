from itertools import combinations, permutations, product

sttr = input()

bool_list = [0, 1]
# --------------------
# Выбираем все заглавные буквы.
set_of_upper_chars = set()
for s in sttr:
    if s.isupper():
        set_of_upper_chars.add(s)
val_list = list(set_of_upper_chars)
val_list.sort()
# --------------------
# Формирует строку для комбинации нулей и единиц что то в виде product(listt, listt, listt), где кол. listt будет равно количеству переменных в верхнем регистре
str_for_product = ""
for k in range(len(val_list) - 1):
    str_for_product += "bool_list, "
else:
    str_for_product += "bool_list"
result_str = "product(" + str_for_product + ")"

# --------------------
# Выводит заголовок
for upper_char in val_list:
    print(upper_char, end=" ")
print("F")
# --------------------
# Выводит саму таблицу
for k in eval(result_str):
    # print(k)
    dictt = dict()
    for i in range(len(val_list)):
        dictt[val_list[i]] = k[i]
    result_for_print = eval(sttr, dictt)
    for z in k:
        print(z, end=" ")
    print(int(result_for_print))


"""
Таблица истинности 2
Продолжим работу с таблицами истинности. Продумайте программу, которая для введённого сложного логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных валидное для языка Python.

Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
В выражении все переменные заданы заглавными латинскими буквами.
Обратите внимание на параметры __globals и __locals у функции eval.

Пример 1
Ввод
not A or B and C
Вывод
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 0
1 1 1 1

Пример 2
Ввод
A and not B and A
Вывод
A B F
0 0 0
0 1 0
1 0 1
1 1 0
"""