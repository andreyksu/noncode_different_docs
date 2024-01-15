# Решено без методов - т.к. по материалу не давали еще методы. Решал так, словно я их бы не знал.
# Решение не очень нравится. Кажется что можно решить проще. Т.е. можно сократить число обходов.

list_of_pair = list()
resut_set = set()
dictt_first_friends = dict()
dictt = dict()

# Собираем данные
while (readed_str := input()) != "":
    tmp_list = readed_str.split()
    list_of_pair.append(tmp_list)
    # Формируем общий список всех ФИО, для обхода.
    for target_person in tmp_list:
        resut_set.add(target_person)

# Сортируем его.
result_list = list(resut_set)
result_list.sort()

# Инициализируем словари.
for pers in result_list:
    dictt_first_friends[pers] = set()
    dictt[pers] = set()

# Формируем словарь человек - первый друг
for target_person in result_list:
    for first_pair in list_of_pair:
        if target_person in first_pair:
            position = first_pair.index(target_person)
            friend = first_pair[position - 1]
            dictt_first_friends[target_person].add(friend)

# Формируем словарь человек - второй друг.
for aim_person in dictt_first_friends:
    for first_friend in dictt_first_friends[aim_person]:
        for second_pair in list_of_pair:
            if first_friend in second_pair:
                position = second_pair.index(first_friend)
                sub_friend = second_pair[position - 1]
                # Если друг первого друга текущий пользователь
                # Или друг друга состоит в первом круге друзей текущего пользователя.
                # Пропускаем и не добавлям его.
                if (
                    sub_friend == aim_person
                    or sub_friend in dictt_first_friends[aim_person]
                ):
                    continue
                dictt[aim_person].add(sub_friend)

# Заменяем в словаре set на list для сортировки.
for aim_person in dictt:
    tmp_set_before_sort = dictt[aim_person]
    sorted_list_sub_friends = list(tmp_set_before_sort)
    sorted_list_sub_friends.sort()
    dictt[aim_person] = sorted_list_sub_friends

# Вывод на печать.
for aim_person in dictt:
    print(f"{aim_person}: ", end="")
    tmp_list_for_print = dictt[aim_person]
    for k in tmp_list_for_print:
        sepp = ", "
        if k == tmp_list_for_print[-1]:
            sepp = ""
        print(f"{k}{sepp}", end="")
    print()


"""
Друзья друзей
Теория шести рукопожатий — социологическая теория, согласно которой любые два человека на Земле разделены не более, чем пятью уровнями общих знакомых (и, соответственно, шестью уровнями связей). Формальная математическая формулировка теории: диаметр графа знакомств не превышает 6. Мы не станем так сильно углубляться в дружественные связи и пока нам хватит только двух уровней. Напишите программу, которая по списку дружественных пар для каждого человека определяет список «друзей 2-го уровня».

Формат ввода
В каждой строке записывается два имени.
Окончанием ввода служит пустая строка.

Формат вывода
Выведите список всех людей и их «друзей 2-го уровня» в формате «Человек: Друг1, Друг2, ...».
Список людей и друзей в каждой строке требуется вывести в алфавитном порядке без повторений.

Пример 1
Ввод
Иванов Петров
Иванов Сергеев
Васильев Петров
Сергеев Яковлев
Петров Кириллов
Петров Яковлев

Вывод
Васильев: Иванов, Кириллов, Яковлев
Иванов: Васильев, Кириллов, Яковлев
Кириллов: Васильев, Иванов, Яковлев
Петров: Сергеев
Сергеев: Петров
Яковлев: Васильев, Иванов, Кириллов
Пример 2
Ввод
Николай Фёдор
Николай Женя
Фёдор Женя
Фёдор Илья
Илья Фёдор

Вывод
Женя: Илья
Илья: Женя, Николай
Николай: Илья
Фёдор: 
"""
