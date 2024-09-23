source_file = input()
even_file = input()
odd_file = input()
eq_file = input()

in_file = open(source_file, encoding="UTF-8")

even_list = list()
odd_list = list()
eq_list = list()

num_line = 0
for line in in_file:
    even_list.append(list())
    odd_list.append(list())
    eq_list.append(list())
    strr = line.rstrip("\n")
    tmp_list = strr.split()
    for word_position in tmp_list:
        odd = 0
        even = 0
        for charr in word_position:
            tmp_int = int(charr)
            if tmp_int % 2 == 0:
                even += 1
            else:
                odd += 1
        else:
            if even == odd:
                eq_list[num_line].append(int(word_position))
            elif even > odd:
                even_list[num_line].append(int(word_position))
            else:
                odd_list[num_line].append(int(word_position))
    num_line += 1
in_file.close()

even_list = [str(sttr_x).strip("[]") + "\n" for sttr_x in even_list]
odd_list = [str(sttr_x).strip("[]") + "\n" for sttr_x in odd_list]
eq_list = [str(sttr_x).strip("[]") + "\n" for sttr_x in eq_list]


def pretty_for_print(target_listt):
    for linee_num in range(len(target_listt)):
        if len(target_listt[linee_num]) <= 1:
            continue
        tmp_str = ""
        current_list = target_listt[linee_num].split(", ")
        for word_position in range(len(current_list) - 1):
            tmp_str += str(current_list[word_position]) + " "
        else:
            tmp_str += str(current_list[-1])
        target_listt[linee_num] = tmp_str


pretty_for_print(even_list)
pretty_for_print(odd_list)
pretty_for_print(eq_list)

with open(even_file, "w", encoding="UTF-8") as file_out_even:
    file_out_even.writelines(even_list)

with open(odd_file, "w", encoding="UTF-8") as file_out_odd:
    file_out_odd.writelines(odd_list)

with open(eq_file, "w", encoding="UTF-8") as file_out_eq:
    file_out_eq.writelines(eq_list)


"""
Разделяй и властвуй
Напишите утилиту, которая разделяет числа, записанные в файле, на три группы:

числа с преобладающим количеством чётных цифр;
числа с преобладающим количеством нечётных цифр;
числа с одинаковым количеством чётных и нечётных цифр.
Формат ввода
Пользователь вводит четыре имени файла.
Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.

Формат вывода
В три другие файла выведите числа, которые подходят под требуемое условие.
Сохраните положение чисел в строках.

Пример
Ввод
# Пользовательский ввод:
numbers.txt
even.txt
odd.txt
eq.txt

# Содержимое файла numbers.txt
650975472 591084323 629700 1504180 577023
8460612246 42161437 29409368 58531725 5725268 2198001838
796451 69358 7195510 975628465 9756641
44200289 126541 979391 93479581 291170 28987042 86139603
Вывод
# Содержимое файла even.txt
629700 1504180
8460612246 29409368 5725268 2198001838
975628465
44200289 28987042

# Содержимое файла odd.txt
650975472 591084323 577023
58531725
796451 69358 7195510 9756641
979391 93479581 291170

# Содержимое файла eq.txt

42161437

126541 86139603

"""
