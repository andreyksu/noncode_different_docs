file_name = input()
line_num = int(input())

in_file = open(file_name, encoding="UTF-8")

listt = list()

for line in in_file:
    listt.append(line)

lenght = len(listt)

if line_num > lenght:
    line_num = lenght


for i in range(lenght - line_num, lenght):
    print(listt[i], end="")


"""
Хвост
В семействе операционных систем Linux существует одна прекрасная консольная утилита — tail. Она предназначена для случаев, когда нам не нужно читать весь файл, а достаточно просмотреть только несколько последних строк.

Напишите аналог этой утилиты.

Формат ввода
Пользователь вводит имя файла (F), а затем количество строк (N), которые он хочет увидеть.

Формат вывода
Выведите N последних строк файла F.

Пример
Ввод
# Пользовательский ввод:
some_file.txt
2

# Содержимое файла some_file.txt
1 строка
2 строка
3 строка
4 строка
5 строка
Вывод
4 строка
5 строка
"""
