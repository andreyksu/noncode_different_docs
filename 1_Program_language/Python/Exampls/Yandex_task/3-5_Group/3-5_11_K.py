import json
# Использую 9_7_G_numbers.txt
in_file_name = input()
out_file_name = input()

file_in = open(in_file_name, encoding="UTF-8")

listt = list()

for line in file_in:
    tmp_str = line.rstrip("\n")
    tmp_list = tmp_str.split()
    listt += [int(x) for x in tmp_list]
file_in.close()

positive_count = 0
for i in listt:
    if i > 0:
        positive_count += 1

count_ = len(listt)
positive_count_ = positive_count
min_ = min(listt)
max_ = max(listt)
sum_ = sum(listt)
avg = sum(listt) / len(listt)
average_ = float(f"{avg:.2f}")

dictt = {
    "count": count_,
    "positive_count": positive_count_,
    "min": min_,
    "max": max_,
    "sum": sum_,
    "average": average_,
}

with open(out_file_name, "w", encoding="UTF-8") as file_out:
    json.dump(dictt, file_out, ensure_ascii=False, indent=4)


"""
Файловая статистика 2.0
Напишите программу, которая для заданного файла вычисляет следующие параметры:

количество всех чисел;
количество положительных чисел;
минимальное число;
максимальное число;
сумма всех чисел;
среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Формат ввода
Пользователь вводит два имени файла.
Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.

Формат вывода
Выведите статистику во второй файл в формате JSON.

Ключи значений задайте соответственно:

count — количество всех чисел;
positive_count — количество положительных чисел;
min — минимальное число;
max — максимальное число;
sum — сумма всех чисел;
average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Пример
Ввод
# Пользовательский ввод:
numbers.txt
statistics.json

# Содержимое файла numbers.txt
1 2 3 4 5
-5 -4 -3 -2 -1
10 20
20 10
Вывод
# Содержимое файла statistics.json
{
    "count": 14,
    "positive_count": 9,
    "min": -5,
    "max": 20,
    "sum": 60,
    "average": 4.29
}
"""