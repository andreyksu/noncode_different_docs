count_of_people = int(input())

listt = list()

for i in range(count_of_people):
    readed_name = input()
    listt.append(readed_name)

sett = set(listt)

count = 0
for j in sett:
    tmp_count = listt.count(j)
    if tmp_count > 1:
        count += tmp_count

print(count)

"""
Однофамильцы
Начальник кадровой службы хочет выяснить, сколько мужчин-однофамильцев работает в организации. У него есть список фамилий, и на основании этого списка нужно вычислить количество фамилий, которые совпадают с другими.

Формат ввода
В первой строке указывается количество мужчин — сотрудников организации (
�
N).
Затем идут 
�
N строк с фамилиями этих сотрудников в произвольном порядке.

Формат вывода
Количество однофамильцев в организации.

Пример 1
Ввод
6
Иванов
Петров
Сидоров
Петров
Иванов
Петров
Вывод
5

Пример 2
Ввод
3
Иванов
Петров
Сидоров
Вывод
0
"""