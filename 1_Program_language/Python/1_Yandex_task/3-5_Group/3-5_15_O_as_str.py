from sys import stdin
import json

file_name = "./Yandex_task/9_Group/9_15_scoring.json"
# file_name = "scoring.json"

with open(file_name, encoding="UTF-8") as file_in:
    dict_form_file = json.load(file_in)

count_of_tests = 0
for test_group in dict_form_file:
    list_of_tests = test_group.get("tests")
    count = len(list_of_tests)
    count_of_tests += count

list_of_answer = list()
"""
for r in range(count_of_tests):
    line = stdin.readline().rstrip("\n")    
    list_of_answer.append(line)
"""
for line in stdin:
    tmp_line = line.rstrip("\n")
    list_of_answer.append(tmp_line.strip())

score = 0
position = 0
for test_group in dict_form_file:
    full_score = test_group.get("points")
    list_of_tests = test_group.get("tests")
    len_of_list_of_tests = len(list_of_tests)
    if len_of_list_of_tests == 0:
        len_of_list_of_tests = 1

    current_score = full_score / len_of_list_of_tests

    for test in list_of_tests:
        test_result = test.get("pattern")
        reslut_from_user = list_of_answer[position]
        position += 1
        if str(reslut_from_user).strip() == str(test_result).strip():
            score += current_score
        # Подходит или нет такое решение через str. С одной строноны нет. т.к. ввод 3.0 не будет равне 3 из файла (т.к. строки).
        # Но с др. стороны так и проверялось в ряде случаев (что, где-то проверялось как есть) - т.е. если ожидается Int а выводится float - то ошибка.

print(int(score))
