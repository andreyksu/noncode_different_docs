count_of_people = int(input())

listt = list()

for i in range(count_of_people):
    readed_name = input()
    listt.append(readed_name)

listt.sort()
dictt = dict()

for i in listt:
    if i in dictt:
        tmp_count = dictt[i]
        dictt[i] = tmp_count + 1
    else:
        dictt[i] = 1

is_present_same_shurname = False
for k in dictt:
    if dictt[k] > 1:
        is_present_same_shurname = True
        print(f"{k} - {dictt[k]}")

if not is_present_same_shurname:
    print("Однофамильцев нет")


"""
Однофамильцы — 2
Вновь поможем сотруднику из отдела кадров выяснить, сколько мужчин-однофамильцев работает в организации, но уже немного с иными условиями.

Формат ввода
В первой строке указывается количество мужчин — сотрудников организации (N).
Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.

Формат вывода
Список однофамильцев в организации с указанием их количества в алфавитном порядке.
Если таковых нет — вывести «Однофамильцев нет».

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
Иванов - 2
Петров - 3

Пример 2
Ввод
3
Иванов
Петров
Сидоров
Вывод
Однофамильцев нет
"""
