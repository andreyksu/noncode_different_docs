the_target_word = "зайка"
sett_of_items = set()

while (readed_str := input()) != "":
    listt = readed_str.split()
    count_of_target_word = listt.count(the_target_word)
    if count_of_target_word == 0:
        continue
    count_of_words = len(listt)
    for i in range(count_of_target_word):
        if the_target_word in listt:
            position = listt.index(the_target_word)
            previous = position - 1
            nextt = position + 1
            # print(f"position = {position}, listt = {listt}, previous = {previous}, next = {nextt}")
            if previous >= 0:
                sett_of_items.add(listt[previous])
            if nextt < len(listt):
                sett_of_items.add(listt[nextt])
            listt = listt[nextt:]
            # print(f"listt = {listt}")
        # print(listt)

for i in sett_of_items:
    print(i)

"""
Зайка — 10
Поможем детям разобраться, что именно они увидели рядом с зайками.

Формат ввода
В каждой строке записано описание придорожной местности.
Конец ввода обозначается пустой строкой.

Формат вывода
Определите список увиденного рядом с зайками без повторений.
Порядок вывода не имеет значения.

Примечание
Считается, что объект находится рядом, если он записан справа или слева от требуемого.

Пример 1
Ввод
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка

Вывод
волк
елочка
медведь
сосна

Пример 2
Ввод
зайка березка
березка зайка
березка елочка березка
елочка елочка елочка

Вывод
березка
"""
