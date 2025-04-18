# Решение сложное. Да и после изменений в handbook превысило время выполнения в 1сек. Пришлось перерешать.

conunt_of_point = int(input())

list_of_points = list()

# Ввод данных.
for i in range(conunt_of_point):
    readed_str = input()
    coordinates_as_list = readed_str.split()
    for k in range(len(coordinates_as_list)):
        coordinates_as_list[k] = int(coordinates_as_list[k])
    list_of_points.append(coordinates_as_list)


x_dict = dict()
y_dict = dict()

for position in range(len(list_of_points)):
    point = list_of_points[position]
    x = point[0]
    y = point[1]
    x_key = x // 10
    y_key = y // 10
    if x_key in x_dict:
        x_dict[x_key].add(position)
    else:
        x_dict[x_key] = {position}

    if y_key in y_dict:
        y_dict[y_key].add(position)
    else:
        y_dict[y_key] = {position}

count_steps = 0

for x_key in x_dict:
    for y_key in y_dict:
        x_set = x_dict[x_key]
        y_set = y_dict[y_key]
        intersect_set = x_set.intersection(y_set)
        range_new_set = len(intersect_set)
        if count_steps < range_new_set:
            count_steps = range_new_set

print(count_steps)

"""
Карта сокровищ
На пиратской карте отмечено N точек, в которых зарыты сокровища. Каждая точка задана координатами (xi​, yi). 
Координаты указаны в километрах. Команда Капитана Крюка хочет составить маршрут, чтобы собрать как можно больше кладов. Однако есть ограничение: для любых двух соседних точек маршрута (xi, yi) и (xj, yj) координаты xi и xj могут различаться только последней цифрой, как и координаты yi и  yj
тоже могут различаться только последней цифрой. Например, после точки (15, 10) они могут отправиться в точку (18, 16), а вот из точки (14, 68) в точку (19, 71) пройти уже не получится, ведь 68 и 71 различаются не только последней цифрой. Из точки (5, 12) в точку (13, 14) попасть тоже нельзя, так как числа 5 и 13 отличаются в разряде десятков. По заданным координатам определите, какое максимальное количество точек сможет добавить в свой маршрут Капитан Крюк.

Формат ввода
В первой строке указано число N (1≤N≤10^5) — количество точек, отмеченных на карте сокровищ. В следующих N строках содержатся пары координат: 
xi и yi — координаты i-ой точки. Координаты — целые числа не меньше нуля и не больше 10^9. Гарантируется, что совпадающих точек в списке нет.

Формат вывода
Выведите одно число — максимальное количество точек, которое Капитан Крюк сможет посетить по маршруту, построенному по описанным правилам.

Пример 1
Ввод
9
10 18
17 15
25 21
0 21
1 16
25 29
24 24
8 26
10 20
Вывод
3

Пример 2
Ввод
3
12 113
114 15
16 117
Вывод
2
"""
