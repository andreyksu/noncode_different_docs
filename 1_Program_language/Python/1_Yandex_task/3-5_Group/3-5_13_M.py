from sys import stdin
import json

file_name = input()

dictt = dict()

for line in stdin:
    splited_parts = line.split("==")
    trimed_pars = [part.strip() for part in splited_parts]
    dictt[trimed_pars[0]] = trimed_pars[1]

with open(file_name, encoding="UTF-8") as file_in:
    records = json.load(file_in)

for keyss in dictt:
    records[keyss] = dictt[keyss]


with open(file_name, "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=4)

"""
Обновление данных
Часто приходится обновлять данные.

Создайте программу, которая обновляет JSON файл.

Формат ввода
Пользователь вводит имя файла.
Затем вводятся строки вида ключ == значение.

Формат вывода
В заданный пользователем файл следует записать обновленный JSON.

Пример
Ввод
# Пользовательский ввод:
data.json
one == один
two == два
three == три

# Содержимое файла data.json
{
    "one": 1,
    "three": 2
}
Вывод
# Содержимое файла data.json
{
    "one": "один",
    "three": "три",
    "two": "два"
}
"""