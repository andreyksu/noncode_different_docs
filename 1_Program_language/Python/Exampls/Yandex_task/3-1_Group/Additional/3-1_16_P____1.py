# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.
# Не проходит решение. Первый и второй тест проходят, а вот третий не проходит.

# Решение усложнено в том плане, что отрезает строку убирая знаки припенания итд (т.е. идём до слова). А в задаче отрезается просто без учёта знаков припенания (где указано, там и отрезано).
# Вероятно из за этого и не проходи остальные тесты, т.к. отрезается разная длина (в задаче орезается буз учётов знаков припенания, а в решении в сучётом знаков припенения)

lenght = int(input())
number_line = int(input())

list_of_lines = list()
lenght_of_lines = 0

str_as_end = "..."

skeep_add_to_list = False
need_to_reduce = False

# Отвечает за ввод данных и формирование списка сторок для обоработки.
for order_line in range(0, number_line):
    readed_str = input()
    if skeep_add_to_list:
        continue
    len_readed_str = len(readed_str)
    lenght_of_lines = lenght_of_lines + len_readed_str
    if lenght_of_lines < lenght - len(str_as_end):
        list_of_lines.append(readed_str)
    else:
        list_of_lines.append(readed_str)
        # Если сюда попали, то нужно будте сокращать сроки.
        need_to_reduce = True
        skeep_add_to_list = True

num_of_lines = len(list_of_lines)
order_line = 0
line_fuzze = True
while (order_line < num_of_lines) and line_fuzze and need_to_reduce:
    order_line += 1
    current_str = list_of_lines.pop()
    # print(f"current_str = {current_str}")
    # Считаем длину оставшихся строк.
    left_str_summ = 0
    for j in list_of_lines:
        left_str_summ = left_str_summ + len(j)
    splited_str = current_str.split(" ", "\t")
    fuzze = True
    j = len(splited_str) - 1
    word_fuzze = True
    while j >= 0 and word_fuzze:
        j -= 1
        last_element = splited_str.pop()
        # print(f"last_element = {last_element}")
        found_position_for_last_element = current_str.rfind(last_element)
        # print(f"found_position_for_last_element = {found_position_for_last_element}")
        last_element_as_char_list = list(last_element)
        # print(f"last_element_as_char_list = {last_element_as_char_list}")
        for k in range(len(last_element_as_char_list)):
            tmp_char = last_element_as_char_list.pop()
            if not tmp_char.isalnum():
                continue
            else:
                intermediate_summ = found_position_for_last_element + (
                    len(last_element) - k
                )
                if left_str_summ + intermediate_summ + len(str_as_end) <= lenght:
                    list_of_lines.append(current_str[:intermediate_summ] + str_as_end)
                    line_fuzze = False
                    word_fuzze = False
                    break
                else:
                    # Обрезаем строку (усекаем, то что не вошло справа).
                    # Пришлось добавить после ошибки с дублирующими словами.
                    current_str = current_str[:found_position_for_last_element]
                    break

# print("-" * 80)
for j in list_of_lines:
    print(j)


"""
40
3
абвгдеёжзи щъьэюя12 щъьэюя12 щъьэюя12 щъьэюя12 щъьэюя12
1234 5678 1а2б 3г4д 5е6ё 7з8и
йцук йцук

Ответ
    абвгдеёжзи...
    
Такой овтет был из за того что без обрезания подстрака (щъьэюя12) всегда находилась с позицией 47 при поиске методом current_str.rfind(last_element)
"""
