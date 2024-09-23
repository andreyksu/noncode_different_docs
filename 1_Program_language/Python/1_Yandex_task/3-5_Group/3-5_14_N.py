import json

first_file = input()
second_file = input()

with open(first_file, encoding="UTF-8") as file_in:
    first_records = json.load(file_in)

with open(second_file, encoding="UTF-8") as file_in:
    second_records = json.load(file_in)

for sec_rec in second_records:
    print(f"i = {sec_rec}")
    s_name = sec_rec.get("name")
    for fir_rec in first_records:
        f_name = fir_rec.get("name")
        if s_name == f_name:
            for key in sec_rec.keys():
                if (fir_rec.get(key) is not None) and (sec_rec[key] < fir_rec[key]):
                    continue
                fir_rec[key] = sec_rec[key]
            break
    else:
        first_records.append(sec_rec)


result_dict = {x.pop("name"): x for x in first_records}

# print(first_records)
# print(result_dict)

with open(first_file, "w", encoding="UTF-8") as file_out:
    json.dump(result_dict, file_out, ensure_ascii=False, indent=4)


"""
Слияние данных
Одна местная компания производит обновление данных о пользователях и заодно решили реорганизовать систему хранения.

Напишите программу, которая обновляет данные о пользователях, записанных в JSON файле.

Формат ввода
Пользователь вводит два имени файла.
В первом хранится JSON массив пользователей.
Во втором — массив новых данных.

Информация о каждом пользователе представляется JSON объектом, в котором обязательно присутствует поле name, описывающее имя пользователя. Остальные поля являются дополнительными.

Формат вывода
В первый файл запишите информацию о пользователях в виде JSON объекта, ключами которого выступают имена пользователей, а значениями — объекты с информацией о них.

Если какая-либо дополнительная информация о пользователе изменяется, то требуется сохранить лексикографически большее значение.

Пример
Ввод
# Пользовательский ввод:
users.json
updates.json

# Содержимое файла users.json
[
    {
        "name": "Ann",
        "address": "Flower st."
    },
    {
        "name": "Bob",
        "address": "Summer st.",
        "phone": "+7 (123) 456-78-90"
    }
]

# Содержимое файла updates.json
[
    {
        "name": "Ann",
        "address": "Awesome st.",
        "phone": "+7 (098) 765-43-21"
    },
    {
        "name": "Bob",
        "address": "Winter st."
    }
]

Вывод
# Содержимое файла users.json
{
    "Ann": {
        "address": "Flower st.",
        "phone": "+7 (098) 765-43-21"
    },
    "Bob": {
        "address": "Winter st.",
        "phone": "+7 (123) 456-78-90"
    }
}
"""