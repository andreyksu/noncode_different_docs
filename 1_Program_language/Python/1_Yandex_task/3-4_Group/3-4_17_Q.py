from itertools import combinations
from itertools import product

target_mast = input()  # Должна присутствовать
target_rank = input()  # Должен отсутстоввать
previous_combination = input()

list_of_rank = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "валет",
    "дама",
    "король",
    "туз",
]
# list_of_mast = ["пик", "треф", "бубен", "червей"]
list_of_mast_n = ["буби", "пики", "трефы", "черви"]  # Именительный
list_of_mast_p = ["бубен", "пик", "треф", "червей"]  # Родительный

position = list_of_mast_n.index(target_mast)
mast = list_of_mast_p[position]

list_of_rank.remove(target_rank)

result_list = list()

for first, second in list(product(list_of_rank, list_of_mast_p)):
    result_list.append(f"{first} {second}")
    
result_list.sort()  # Для лексеграфической сортировки

need_print = False
for first, second, third in combinations(result_list, 3):
    if (mast in first or mast in second or mast in third):
        result_sttr = f"{first}, {second}, {third}"
        if previous_combination == result_sttr:
            need_print = True
            continue
        if need_print:
            print(result_sttr)
            break
        
"""
А есть ещё варианты?
Давайте вновь поможем Виталию выяснить, какие вариации вытащить из колоды определённые тройки карт возможны. Напишите программу, которая выводит список вариантов согласно требованиям.

Формат ввода
В первой строке записана масть, которая должна присутствовать в тройке. Во второй строке записан достоинство, которого не должно быть в тройке. В третьей строке записан предыдущий вариант полученный Виталием.

Формат вывода
Выведите следующий вариант расклада.

Примечание
Обратите внимание: валет-дама-король-туз лексикографически упорядочены. Но «10 ...» лексикографически младше, чем «2 ...», а бубны младше, чем пики.

Масти в именительном и родительном падежах:

Именительный	Родительный
буби	бубен
пики	пик
трефы	треф
черви	червей
Пример 1
Ввод
пики
10
9 пик, король треф, туз червей
Вывод
9 пик, король червей, туз бубен

Пример 2
Ввод
трефы
король
2 червей, туз пик, туз треф
Вывод
2 червей, туз треф, туз червей
"""