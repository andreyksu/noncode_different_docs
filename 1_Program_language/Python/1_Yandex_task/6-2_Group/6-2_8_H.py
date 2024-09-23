import numpy as np
import pandas as pd


def update(aa_frame):
    count_column = 3
    a_frame = aa_frame.copy()
    a_frame["average"] = (
        a_frame["maths"] + a_frame["physics"] + a_frame["computer science"]
    ) / count_column
    a_frame.sort_values(
        by=["average", "name"],
        axis=0,
        ascending=[False, True],
        inplace=True,
        kind="quicksort",
    )
    return a_frame


columns = ["name", "maths", "physics", "computer science"]
data = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)


"""
Обновление журнала

Продолжим обрабатывать DataFrame из прошлых задач.

Напишите функцию update, которая добавляет к данным столбец average, содержащий среднюю оценку ученика, а также сортирует данные по убыванию этого столбца, а при равенстве средних — по имени лексикографически.
Примечание

Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.
Пример
Ввод

columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)

Вывод

       name  maths  physics  computer science
0    Иванов      5        4                 5
1    Петров      4        4                 2
2   Сидоров      5        4                 5
3  Васечкин      2        5                 4
4  Николаев      4        5                 3
       name  maths  physics  computer science   average
0    Иванов      5        4                 5  4.666667
2   Сидоров      5        4                 5  4.666667
4  Николаев      4        5                 3  4.000000
3  Васечкин      2        5                 4  3.666667
1    Петров      4        4                 2  3.333333

"""
