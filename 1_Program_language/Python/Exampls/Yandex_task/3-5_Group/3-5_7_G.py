file_name = input()

# c:\Utils\Code\different_docs\1_Program_language\Python\Exampls\Yandex_task\9_Group\9_7_G_numbers.txt
# ./Yandex_task/9_Group/9_7_G_numbers.txt
# print(file_name)

file_in = open(file_name, encoding="UTF-8")

listt = list()

for line in file_in:
    tmp_str = line.rstrip("\n")
    tmp_list = tmp_str.split()
    listt += [int(x) for x in tmp_list]
file_in.close()

print(len(listt))

positive_count = 0
for i in listt:
    if i > 0:
        positive_count += 1

print(positive_count)
print(min(listt))
print(max(listt))
print(sum(listt))
avg = sum(listt) / len(listt)
print(f"{avg:.2f}")

'''
Файловая статистика
Напишите программу, которая для заданного файла вычисляет следующие параметры:

количество всех чисел;
количество положительных чисел;
минимальное число;
максимальное число;
сумма всех чисел;
среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Формат ввода
Пользователь вводит имя файла.
Файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.

Формат вывода
Выведите статистику в указанном порядке.

Пример
Ввод
# Пользовательский ввод:
numbers.txt

# Содержимое файла numbers.txt
1 2 3 4 5
-5 -4 -3 -2 -1
10 20
20 10
Вывод
14
9
-5
20
60
4.29
'''