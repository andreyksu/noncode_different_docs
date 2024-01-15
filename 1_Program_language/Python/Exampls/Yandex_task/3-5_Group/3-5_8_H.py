first_txt_file = input()
second_txt_file = input()
third_txt_file = input()

file_in = open(first_txt_file, encoding="UTF-8")

listt = list()

for line in file_in:
    tmp_str = line.rstrip("\n")
    tmp_list = tmp_str.split()
    listt += tmp_list
file_in.close()

first_set = set(listt)

file_in = open(second_txt_file, encoding="UTF-8")

listt = list()

for line in file_in:
    tmp_str = line.rstrip("\n")
    tmp_list = tmp_str.split()
    listt += tmp_list
file_in.close()

second_set = set(listt)

reslut_set = first_set ^ second_set

result_list = list(reslut_set)
result_list.sort()
list_to_print = [str(x) + "\n" for x in result_list]

file_out = open(third_txt_file, "w", encoding="UTF-8")
file_out.writelines(list_to_print)
file_out.close()

"""
./Yandex_task/9_Group/9_8_H_first.txt
./Yandex_task/9_Group/9_8_H_second.txt
./Yandex_task/9_Group/9_8_H_third.txt
"""

"""
Формат ввода
Пользователь вводит три имени файлов.
Каждый из входных файлов содержит произвольное количество слов, разделённых пробелами и символами перевода строки.

Формат вывода
В третий файл выведите в алфавитном порядке без повторений список слов, которые есть только в одном из файлов.

Пример
Ввод
# Пользовательский ввод:
first.txt
second.txt
answer.txt

# Содержимое файла first.txt
кофе молоко
чай печенье
велосипед

# Содержимое файла second.txt
кофе велосипед
пряник жвачка весло

Вывод
# Содержимое файла answer.txt
весло
жвачка
молоко
печенье
пряник
чай
"""