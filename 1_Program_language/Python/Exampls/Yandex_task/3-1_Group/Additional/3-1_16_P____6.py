# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.
# Не проходит решение. Первый и второй тест проходят, а вот третий не проходит.

lenght = int(input())
number_line = int(input())

list_for_print = list()

the_end = "..."

full_lenght = 0

fuzze = True
lookBack = False
for i in range(1, number_line + 1):
    current_str = input()
    if not fuzze:
        continue
    lenght_current_str = len(current_str)
    previous = full_lenght
    full_lenght = full_lenght + lenght_current_str
    delta = (lenght - 3) - previous
    if (
        full_lenght >= (lenght - len(the_end))
        and (full_lenght <= lenght)
        and i < number_line
    ):
        tmp_strr = current_str[:delta] + the_end
        list_for_print.append(tmp_strr)
        lookBack = True
        fuzze = False
    elif full_lenght > lenght - len(the_end):
        tmp_strr = current_str[:delta] + the_end
        list_for_print.append(tmp_strr)
        fuzze = False
    elif full_lenght <= lenght:
        list_for_print.append(current_str)
        # print(f"list_for_print = {list_for_print}")
    else:
        bound = (full_lenght - lenght) + len(the_end)
        list_for_print.append(current_str[: (-1) * bound] + the_end)
        fuzze = False

for i in list_for_print:
    print(i)
