# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

# ### - Означает(требуется оптимизация) - решение не очень нравится
# Переосмыслить - не очень нравится решение.
# Не нравится решение, т.к. два одинковых цикла И мне кажется что можно оптимизировать + бесконечное суммирование к строке тоже не очень хорошо.
target_num = int(input())

# Да, это лишнее. Здесь тольк поиск максимальной строки. Для центрирования относительно неё. Но с др. Стороны как без неё, ведь длину нужно знать перед выводом.
# По сути если знать коллекции, то можно на этом этапе сложить в коллекции те строки, что получилиось и их испльзовать при печате (но вопрос про расход памяти если очень много).
number_in_line = 0
increment = 1
fuzze = True
lenn = 0
while fuzze:
    number_in_line += 1
    last_str = ""
    for i in range(1, number_in_line + 1):
        last_str = last_str + str(increment) + " "
        increment += 1
        if increment >= target_num + 1:
            fuzze = False
            break
    lenn_tmpp = len(last_str) - 1
    if lenn < lenn_tmpp:
        lenn = lenn_tmpp

number_in_line_1 = 0
increment_1 = 1
fuzze_1 = True
while fuzze_1:
    number_in_line_1 += 1
    str_for_print = ""
    for i in range(1, number_in_line_1 + 1):
        if i == 1:
            delimeter = ""
        else:
            delimeter = " "
        str_for_print = str_for_print + delimeter + str(increment_1)
        increment_1 += 1
        if increment_1 >= target_num + 1:
            fuzze_1 = False
            break
    print(f"{str_for_print:^{lenn}}")


"""
Новогоднее настроение 2.0
Коллеги математика вновь хотят порадовать его и сделать математические ёлки, которые украсят кабинет учёного.
Помогите им, написав программу, которая по введённому числу строит математическую ёлку.

Формат ввода
Вводится одно натуральное число — количество чисел в математической ёлке.

Формат вывода
Требуемая новогодня ёлка.

Примечание
Не забывайте про существование f-строк.

В данный момент визуализация примеров работает не корректно.
Ответ на первый тест должен выглядеть так:

     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14

Пример 1
Ввод
14
Вывод
     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14

Пример 2
Ввод
6
Вывод
  1  
 2 3 
4 5 6
"""
