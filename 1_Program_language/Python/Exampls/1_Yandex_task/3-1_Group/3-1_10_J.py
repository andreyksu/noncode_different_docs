# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.
listt = list()

barrier = "ФИНИШ"

# Читаем строки и формируем список списков (вложенный список это 2а элемента. Первый - символ, Второй - частота повторения). Если такого символа нет в нашем списке, то добавлеяем его. Если есть, то к частоте прибавляем 1.

while (readed := input()) != barrier:
    readed = str(readed).lower()
    for i in readed:
        i = str(i)
        if i.isalpha() or i.isdigit():
            for j in listt:
                if j[0] == i:
                    j[1] = j[1] + 1
                    break
            else:
                listt.append([i, 1])

max_ocure = 0
char = None
for i in listt:
    if i[1] > max_ocure:
        max_ocure = i[1]
        char = i[0]
    elif i[1] == max_ocure and i[0] < char:
        max_ocure = i[1]
        char = i[0]

print(char)


"""
Частотный анализ на минималках
Частотный анализ — подсчёт, какие символы чаще всего встречаются в тексте. Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря и до шифровальной машины «Энигма». Выполним простой частотный анализ: выясним, какой символ встречается в тексте чаще всего.

Формат ввода
Вводятся строки, пока не будет введена строка «ФИНИШ».

Формат вывода
Выводится один символ в нижнем регистре — наиболее часто встречающийся.

Примечания
Пробелы в анализе не участвуют.
Если в результате анализа получено несколько ответов, следует вывести первый по алфавиту.

Пример 1
    Ввод
    Баобаб
    Белка
    Бобы
    ФИНИШ
    Вывод
    б
Пример 2
    Ввод
    Финики Фокачча Зайка
    Филин Фосфор Светофор
    Фехтовальщик Форма
    ФИНИШ
    Вывод
    ф
"""