from itertools import combinations, permutations, product

sttr = input()

bool_list = [0, 1]
# --------------------
# Выбираем все заглавные буквы.
set_of_upper_chars = set()
for s in sttr:
    if s.isupper():
        set_of_upper_chars.add(s)
list_of_char = list(set_of_upper_chars)
list_of_char.sort()
# --------------------
str_for_product = ""
for combination in range(len(list_of_char) - 1):
    str_for_product += "bool_list, "
else:
    str_for_product += "bool_list"
str_for_product_eval = "product(" + str_for_product + ")"

print(f"list_of_char = {list_of_char}")
print(f"str_for_product_eval = {str_for_product_eval}")
# --------------------
# Выводит заголовок
for charr in list_of_char:
    print(charr, end=" ")
print("F")
# --------------------
# Выводит саму таблицу
for combination in eval(str_for_product_eval):
    print(f"combination = {combination}")
    dict_to_eval = dict()
    for position, targ_char in enumerate(list_of_char):
        dict_to_eval[targ_char] = combination[position]
    print(f"dict = {dict_to_eval}")
    resul_of_eval = eval(sttr, dict_to_eval)
    for val_in_combination in combination:
        print(val_in_combination, end=" ")
    print(int(resul_of_eval))


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