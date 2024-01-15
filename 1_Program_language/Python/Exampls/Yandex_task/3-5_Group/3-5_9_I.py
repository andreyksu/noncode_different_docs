first_file = input()
second_file = input()

file_in = open(first_file, encoding="UTF-8")

listt = list()

for line in file_in:
    in_str = line.rstrip("\n") # С ходу убираем переводы строк (соответственно удалим сразу и пестые строки)
    in_str = in_str.strip() # С ходу убираем по краям пробелы. Вероятно и табы нужно почистить.
    in_str = in_str.strip("\t") # Будто не обязательно.
    if len(in_str) < 1:
        continue
    splited_list = in_str.split("\t")
    result_str = ""
    for word in splited_list: #Разделили по Tab и соединяем без всего.
        result_str += word

    splited_list = result_str.split()
    result_str = ""
    for position in range(len(splited_list) - 1): # Разделили по проблема и соединяем с одним пробелом.
        result_str += splited_list[position] + " "
    else:
        result_str += splited_list[-1]
    listt.append(result_str) # Добавляем строку в список.
file_in.close()

listt = [str(x) + "\n" for x in listt] #Добавляем к строкам перевод строк.
listt[-1] = listt[-1].rstrip("\n") # У последней строки удаляем перевод строк.

file_out = open(second_file, "w", encoding="UTF-8")
file_out.writelines(listt)
file_out.close()

"""
Файловая чистка
Python в первую очередь скриптовый язык. Такие языки часто используются для создания консольных утилит.

Напишите простую утилиту, которая очищает заданный файл от:

повторяющихся пробелов;
повторяющихся символов перевода строки;
табуляций,
излишних пробелов в начале и конце строк.
Формат ввода
Пользователь вводит два имени файлов.
Входной файл содержит неформатированный текст произвольной длины.

Формат вывода
Во второй файл выведите очищенный текст.

Пример
Ввод
# Пользовательский ввод:
first.txt
second.txt

# Содержимое файла first.txt
    очень 		 плохо форматированный       текст


ну		ну	
прямо

очень-очень

	
Вывод
# Содержимое файла second.txt
очень плохо форматированный текст
нуну
прямо
очень-очень

"""