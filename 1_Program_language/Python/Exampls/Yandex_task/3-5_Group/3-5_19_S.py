shift = int(input())

list_of_alfabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

if abs(shift) > len(list_of_alfabet):
    result_shift = abs(shift) % len(list_of_alfabet)
    if shift >= 0:
        shift = result_shift
    else:
        shift = result_shift * (-1)


# file_name_in = "./Yandex_task/9_Group/9_19_S_public.txt"
file_name_in = "public.txt"
# file_name_out = "./Yandex_task/9_Group/9_19_S_private.txt"
file_name_out = "private.txt"

list_of_line = list()
with open(file_name_in, encoding="UTF-8") as file_in:
    for line_num in file_in:
        list_of_line.append(line_num)

for line_num in range(len(list_of_line)):
    list_for_accumulate = list()
    for charr in list_of_line[line_num]:
        current_char = str(charr)
        if current_char.isalpha():
            is_apper_case = current_char.isupper()
            tmp_charr = current_char.lower()
            position = list_of_alfabet.index(tmp_charr)
            currn_pos = position + shift
            if currn_pos >= len(list_of_alfabet):
                currn_pos = currn_pos % len(list_of_alfabet)
            shifted_char = list_of_alfabet[currn_pos]
            if is_apper_case:
                shifted_char = shifted_char.upper()
            list_for_accumulate.append(shifted_char)
        else:
            list_for_accumulate.append(current_char)
    result_str = "".join(list_for_accumulate)
    list_of_line[line_num] = result_str

with open(file_name_out, "w", encoding="UTF-8") as file_out:
    file_out.writelines(list_of_line)


"""
Это будет наш секрет
Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один из самых простых и наиболее широко известных методов шифрования. Он назван в честь римского полководца Гая Юлия Цезаря, использовавшего его для секретной переписки со своими генералами.

Давайте реализуем эту систему шифрования. Однако для простоты мы будем сдвигать только латинские символы по кругу.

Формат ввода
Вводится размер сдвига для шифрования.

В файле public.txt содержится текст на английском языке.

Формат вывода
В файл private.txt запишите зашифрованный текст.

Пример 1
Ввод
# Пользовательский ввод
3

# Содержимое файла public.txt
Hello, world!
Вывод
# Содержимое файла private.txt
Khoor, zruog!
Пример 2
Ввод
# Пользовательский ввод
-10

# Содержимое файла public.txt
English alphabet: ABCDEFG...XYZ
Вывод
# Содержимое файла private.txt
Udwbyix qbfxqruj: QRSTUVW...NOP
"""