count_of_children = int(input())

dict_of_preference = dict()

for i in range(count_of_children):
    readed_str = input()
    tmpp = readed_str.split()
    name = tmpp[0]
    for i in range(1, len(tmpp)):
        current_porridge = tmpp[i]
        if current_porridge not in dict_of_preference:
            dict_of_preference[current_porridge] = [name]
        else:
            tmp_list = dict_of_preference[current_porridge]
            tmp_list.append(name)


target_porridge = input()

# print(dict_of_preference)

if target_porridge in dict_of_preference:
    list_of_children = dict_of_preference[target_porridge]
    list_of_children.sort()
    # print(list_of_children)
    for i in list_of_children:
        print(i)
else:
    print("Таких нет")


"""
Кашееды — 4
Каждый воспитанник детского сада любит одну или несколько каш.
Поможем воспитателю составить список детей, которые любят конкретную кашу.

Формат ввода
В первой строке задаётся количество детей в группе (
�
N). В следующих 
�
N строках записана фамилия ребенка и список его любимых каш. В последней строке записана каша, информацию о которой хочет получить воспитатель.

Формат вывода
Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
Если таких не окажется, в строке вывода нужно написать «Таких нет».

Пример 1
Ввод
5
Васильев манная
Петров манная
Васечкин манная
Иванов овсяная
Михайлов овсяная
манная
Вывод
Васечкин
Васильев
Петров

Пример 2
Ввод
3
Иванов манная овсяная
Петров манная овсяная
Васечкин манная овсяная
гречневая
Вывод
Таких нет
"""