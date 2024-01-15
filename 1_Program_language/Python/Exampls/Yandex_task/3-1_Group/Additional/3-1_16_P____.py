# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.
# Проходит только два первых теста и всё.

# Решение не нравится, как -то кажется не очень удачным или очень неудачным.

# Решение усложнено в том плане, что отрезает строку убирая знаки припенания итд (т.е. идём до слова). А в задаче отрезается просто без учёта знаков припенания (где указано, там и отрезано).
# Вероятно из за этого и не проходи остальные тесты, т.к. отрезается разная длина (в задаче орезается буз учётов знаков припенания, а в решении в сучётом знаков припенения)

lenght = int(input())
number_line = int(input())

listt = list()
current_lenght = 0

the_end = "..."

skeep = False

for i in range(0, number_line):
    strr = input()
    if skeep:
        continue
    tmp_lenght = len(strr)
    current_lenght = current_lenght + tmp_lenght
    if current_lenght < lenght - len(the_end):
        listt.append(strr)
    else:
        skeep = True
        deductible = current_lenght - (lenght + len(the_end))
        tmp_str = ""
        if tmp_lenght <= len(the_end):
            tmp_str = listt.pop()
        else:
            tmp_str = strr[0 : tmp_lenght - deductible]

        meet_white_space = False
        for j in range(len(tmp_str) - 1, -1, -1):
            tmp_char = tmp_str[j]
            if tmp_char.isalnum():
                if j < len(the_end):
                    continue
                elif j >= len(the_end) and meet_white_space:
                    result_len = 0
                    for k in listt:
                        result_len = result_len + len(k)
                    result_len = len(tmp_str) - (len(tmp_str) - j) + len(the_end)
                    if result_len > lenght:
                        continue
                    tmp_str = strr[0 : j + 1] + the_end
                    break
            else:
                meet_white_space = True
                continue

        listt.append(tmp_str)

for j in listt:
    print(j)
