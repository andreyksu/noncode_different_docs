# Принятое решение. Не нужно было приводить переменные reslut_from_user и test_result к float.
from sys import stdin
import json

file_name = "./Yandex_task/9_Group/9_15_scoring.json"
# file_name = "scoring.json"

with open(file_name, encoding="UTF-8") as file_in:
    first_records = json.load(file_in)

count_of_tests = 0
for test_group in first_records:
    list_of_tests = test_group.get("tests")
    count = len(list_of_tests)
    count_of_tests += count

list_of_answer = list()
"""
for r in range(count_of_tests):
    line = stdin.readline()
    # Здесь cast to int, или потом?
    list_of_answer.append(line)
"""
for line in stdin:
    list_of_answer.append(line.rstrip("\n"))

score = 0
position = 0
for test_group in first_records:
    full_score = test_group.get("points")
    list_of_tests = test_group.get("tests")
    len_list_of_test = len(list_of_tests)
    if len_list_of_test == 0:
        len_list_of_test = 1

    current_score = full_score / len_list_of_test

    for test in list_of_tests:
        test_result = test.get("pattern")
        reslut_from_user = list_of_answer[position]
        position += 1
        if str(reslut_from_user).strip() == str(test_result).strip():
            score += current_score

print(int(score))

"""

"""