number_love_semolina = int(input())
number_love_oatmeal = int(input())

common_dict = dict()
common_number_of_children = number_love_semolina + number_love_oatmeal

for i in range(common_number_of_children):
    tmp_str = input()
    if tmp_str in common_dict:
        count = common_dict[tmp_str]
        common_dict[tmp_str] = count + 1
    else:
        common_dict[tmp_str] = 1

number_singer_love = 0
for i in common_dict:
    if common_dict[i] == 1:
        number_singer_love += 1

if number_singer_love == 0:
    print("Таких нет")
else:
    print(number_singer_love)


"""
Пересечение первого и второго набора не подходит, т.к. фамилии в перемешку.
Т.е. может быть так 

Ввод
3
2
Васильев
Петров
Васечкин
Иванов
Иванов
"""

"""
Кашееды — 2
Изменим задачу и напишем программу, которая поможет быстро выяснить, сколько детей любят только одну кашу.

Формат ввода
В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
Затем идут N+M строк — перемешанные фамилии детей.
Гарантируется, что в группе нет однофамильцев.

Формат вывода
Количество учеников, которые любят только одну кашу.
Если таких не окажется, в строке вывода нужно написать «Таких нет».

Пример 1
Ввод
3
2
Васильев
Петров
Васечкин
Иванов
Михайлов
Вывод
5

Пример 2
Ввод
3
3
Иванов
Петров
Васечкин
Иванов
Петров
Васечкин
Вывод
Таких нет
"""
