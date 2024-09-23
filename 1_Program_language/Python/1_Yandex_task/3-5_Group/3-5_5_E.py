from sys import stdin

listt = list()

for line in stdin:
    tmp_str = line.rstrip("\n")
    tmp_list = tmp_str.split()
    for word in tmp_list:
        # print(f"word = {word}")
        lenght = len(word)
        half = lenght // 2
        for i in range(half):
            left_side = i
            right_side = (-1 * i) - 1
            if word[left_side].lower() != word[right_side].lower():
                break
        else:
            # print(f"append to list = {word}")
            listt.append(word)

listt = list(set(listt))
listt.sort()

for i in listt:
    print(i)


"""
А роза упала на лапу Азора 6.0
Мы уже писали программы, которые определяли, а палиндром перед нами или нет.
Давайте теперь найдём все слова-палиндромы среди введённых строк.

Формат ввода
Вводятся слова.

Формат вывода
Список слов-палиндромов в алфавитном порядке без повторений.

Примечание
При проверке слов не обращайте внимание на регистр.

Пример
Ввод
Анна Боря Вова
Я последняя буква алфавита
Дед строит шалаш
Шалаш был хорош
Дед слышит топот
Ара залетел в шалаш
Вывод
Анна
Ара
Дед
Шалаш
Я
в
топот
шалаш
"""