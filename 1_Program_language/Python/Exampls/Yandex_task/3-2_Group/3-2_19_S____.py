# Решение не нравится, т.к. перекладываю из коллекции в коллекцию много раз.
# Очень не нравится решение.

count_of_children = int(input())

list_of_sets = list()
result_list = list()

# Читаем ввод и формируем коллекцию входных данндых (список множеств, где множества это игрушки конкретного ребёнка)
for i in range(count_of_children):
    readed_str = input()
    splited_str = readed_str.split(":")
    toys = splited_str[-1]
    list_of_toys = toys.split(",")
    for kk in range(len(list_of_toys)):
        tmppElement = list_of_toys[kk]
        list_of_toys[kk] = tmppElement.strip()
    set_of_toys = set(list_of_toys)
    list_of_sets.append(list(set_of_toys))

# Для каждого множества
for position_1_of_set in range(len(list_of_sets)):
    current_set = list_of_sets[position_1_of_set]
    # Для каждого элемента множества
    for position_of_item in range(len(current_set)):
        is_present_element = False
        # Проверяем вхождение этого элемента в чужие множества. Своё множество пропускаем.
        for position_2_of_set in range(len(list_of_sets)):
            if position_1_of_set == position_2_of_set:
                continue
            if current_set[position_of_item] in list_of_sets[position_2_of_set]:
                is_present_element = True
                break
        else:
            # Если вхождения элемента в чужие множества нет, то сохраняем данный элемент в списке.
            result_list.append(current_set[position_of_item])

result_list.sort()
for i in result_list:
    print(i)


"""
Частная собственность
Ребята приносят игрушки в детский сад и играют все вместе.
Сегодня они решили выяснить, игрушки какого типа принадлежат только одному из детей. Напишите программу, которая по списку детей и их игрушек определит «частную собственность».

Формат ввода
В первой строке задается количество детей в группе (N).
В каждой из следующих N строк записано имя ребенка и его игрушки в формате:
Имя: игрушка1, игрушка2, ....

Формат вывода
Список игрушек, которые есть только у одного из детей в алфавитном порядке.

Пример
Ввод
3
Аня: кукла, машинка, кукла, домик
Боря: машинка, зайчик
Вова: кубики, машинка
Вывод
домик
зайчик
кубики
кукла
"""
