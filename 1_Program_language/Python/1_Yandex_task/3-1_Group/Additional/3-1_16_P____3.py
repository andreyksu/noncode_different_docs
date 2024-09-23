# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.
# Не проходит решение. Первый и второй тест проходят, а вот третий не проходит.

# Решение усложнено в том плане, что отрезает строку убирая знаки припенания итд (т.е. идём до слова). А в задаче отрезается просто без учёта знаков припенания (где указано, там и отрезано).
# Вероятно из за этого и не проходи остальные тесты, т.к. отрезается разная длина (в задаче орезается буз учётов знаков припенания, а в решении в сучётом знаков припенения)
# Здесь в в решение добавлено еще и работу со знаками припенания !!! -> !..

lenght = int(input())
number_line = int(input())

list_of_lines = list()
lenght_of_lines = 0

str_as_end = "..."
str_as_end_short = ".."
str_as_end_ext_short = "."

skeep_add_to_list = False
need_to_reduce = False

# Отвечает за ввод данных и формирование списка сторок для обоработки.
for num_line in range(0, number_line):
    readed_str = input()
    if skeep_add_to_list:
        continue
    len_readed_str = len(readed_str)
    lenght_of_lines = lenght_of_lines + len_readed_str
    if lenght_of_lines < lenght:
        list_of_lines.append(readed_str)
    else:
        list_of_lines.append(readed_str)
        # Если сюда попали, то хватит наполнять List.
        skeep_add_to_list = True
        # Если сюда попали, то нужно будет сокращать/обрезать сроку.
        need_to_reduce = True

# print(f"list_of_lines = {list_of_lines}")
for i in list_of_lines:
    if len(i) > 0:
        tmp_splited_str = i.split()
        first_tmp_word = tmp_splited_str[0]
        if len(first_tmp_word) >= lenght - len(str_as_end):
            list_of_lines[0] = first_tmp_word[: lenght - len(str_as_end)] + str_as_end
            line_fuzze = False
            word_fuzze = False
            break

num_of_lines = len(list_of_lines)
line_fuzze = True
order_line = 0
while (order_line < num_of_lines) and line_fuzze and need_to_reduce:
    order_line += 1
    current_line = list_of_lines.pop()
    # Считаем длину оставшихся строк.
    left_str_summ = 0
    for j in list_of_lines:
        left_str_summ = left_str_summ + len(j)
    splited_current_line = current_line.split(" ")
    fuzze = True
    j = len(splited_current_line) - 1
    word_fuzze = True
    while j >= 0 and word_fuzze:
        j -= 1
        last_word = splited_current_line.pop()
        found_position_for_last_element = current_line.rfind(last_word)

        # Это все касается проставки точек для случая ? ! ?!  ---> ?.. !.. ?!.
        # Но будет проблема с подсчетом если эти знаки будут в середине слова "сло?во" - что делать с такими словами?

        last_word_as_char_list = list(last_word)
        count_of_spetial_char = 0
        ending_of_str = ""
        for k in range(len(last_word_as_char_list)):
            tmp_char = last_word_as_char_list.pop()
            if not tmp_char.isalnum():
                if tmp_char in ("!", "?", "."):
                    count_of_spetial_char += 1
                    ending_of_str = tmp_char + ending_of_str
                else:
                    # Если имеем "string!!-!!!" - то скидываем счетчик при встрече "-" и начинаем считать снова.
                    count_of_spetial_char = 0
                    ending_of_str = ""
                    pass
                continue
            if count_of_spetial_char >= 3:
                ending_of_str = ending_of_str[:3]
                tmp_end = ending_of_str
            elif count_of_spetial_char == 2:
                tmp_end = ending_of_str + str_as_end_ext_short
            elif count_of_spetial_char == 1:
                tmp_end = ending_of_str + str_as_end_short
            else:
                tmp_end = str_as_end
            # print(f"count_of_spetial_char = {count_of_spetial_char}, tmp_end = {tmp_end}")
            intermediate_summ = found_position_for_last_element + (len(last_word) - k)
            if left_str_summ + intermediate_summ + len(tmp_end) <= lenght:
                list_of_lines.append(current_line[:intermediate_summ] + tmp_end)
                line_fuzze = False
                word_fuzze = False
                break
            else:
                # Обрезаем строку (усекаем, то что не вошло справа).
                # Пришлось добавить после ошибки с дублирующими словами.
                current_line = current_line[:found_position_for_last_element]
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
