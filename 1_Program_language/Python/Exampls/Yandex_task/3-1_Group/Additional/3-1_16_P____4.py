# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.
# Не проходит решение. Первый и второй тест проходят, а вот третий не проходит.

# Решение усложнено в том плане, что отрезает строку убирая знаки припенания итд (т.е. идём до слова). А в задаче отрезается просто без учёта знаков припенания (где указано, там и отрезано).
# Вероятно из за этого и не проходи остальные тесты, т.к. отрезается разная длина (в задаче орезается буз учётов знаков припенания, а в решении в сучётом знаков припенения)

lenght = int(input())
number_line = int(input())

list_for_print = list()

the_end = "..."

full_lenght = 0

fuzze = True

for i in range(0, number_line):
    current_str = input()
    if not fuzze:
        continue
    lenght_current_str = len(current_str)
    full_lenght = full_lenght + lenght_current_str
    if full_lenght < (lenght):
        list_for_print.append(current_str)
        print(f"list_for_print = {list_for_print}")
    else:
        bound = (full_lenght - lenght) + len(the_end)
        list_for_print.append(current_str[: (-1) * bound] + the_end)
        fuzze = False

for i in list_for_print:
    print(i)
