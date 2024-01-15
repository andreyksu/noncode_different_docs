# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.

inputed_str = input()

str_to_lower_case = inputed_str.lower()
listt = str_to_lower_case.split()
new_str = "".join(listt)

whole_lenl_of_str = len(new_str)

helf = whole_lenl_of_str // 2
first_helf_of_str = new_str[:helf]
second_helf_of_str = ""
if whole_lenl_of_str % 2 == 0:
    second_helf_of_str = new_str[helf:]
else:
    second_helf_of_str = new_str[helf + 1:]

reversed_second_helf_of_str = second_helf_of_str[::-1]

if first_helf_of_str == reversed_second_helf_of_str:
    print("YES")
else:
    print("NO")


"""
А роза упала на лапу Азора 5.0
И снова напишем программу, которая определяет, палиндромом перед нами или нет.

Формат ввода
Вводится строка.

Формат вывода
Если введённая строка относится к палиндрому, то вывести YES, а иначе — NO.

Примечание
При проверке не обращайте внимания на регистр и пробелы.

Пример 1
    Ввод
    А роза упала на лапу Азора
    Вывод
    YES
Пример 2
    Ввод
    Мама мыла раму
    Вывод
    NO
"""
