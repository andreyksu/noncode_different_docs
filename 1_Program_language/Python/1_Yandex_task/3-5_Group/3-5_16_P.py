from sys import stdin

files_with_target_string = []

lines = []
for line in stdin:
    lines.append(line)

lines = [x.strip("\n") for x in lines]

target_string = lines[0].lower()

files = lines[1:]

for file in files:
    with open(file, "r", encoding="UTF-8") as file_in:
        readed_lines_raw = file_in.readlines()
        readed_lines = " ".join(readed_lines_raw)
        lower_reade_lines = readed_lines.lower()
        intermediate = lower_reade_lines.replace("&nbsp;", " ").replace("\n", " ")
        intermediate = intermediate.split(" ")
        new_strr = [x for x in intermediate if x]
        target_strr = " ".join(new_strr)
        if target_string in target_strr:
            files_with_target_string.append(file)

if files_with_target_string:
    for i in files_with_target_string:
        print(i)
else:
    print("404. Not Found")

"""
Найдётся всё 3.0

Давайте вновь напишем небольшой компонент поисковой системы.

Формат ввода
Сначала вводится поисковый запрос.
Затем вводятся имена файлов, среди которых следует произвести поиск.

Формат вывода
Выведите все имена файлов, в которых есть поисковая строка без учета регистра и повторяющихся пробельных символов.
Если ни в одном файле информация не была найдена, выведите "404. Not Found".

Примечание
Система поиска должна обрабатывать строки "a&nbsp;&nbsp;&nbsp;&nbsp;b", "a b" и "a\nb" как одинаковые.

Пример 1
Ввод
# Пользовательский ввод:
    Мама мыла РАМУ
    first.txt
    second.txt

# Содержимое файла first.txt
    В этом файле говорится    о том что МАМА   

    мылА
    Раму

# Содержимое файла second.txt
    А в этом не говорится

Вывод
    first.txt

Пример 2
Ввод
# Пользовательский ввод:
    Python
    only_one_file.txt

# Содержимое файла only_one_file.txt
    Тут нет никаких змей

Вывод
    404. Not Found

"""
