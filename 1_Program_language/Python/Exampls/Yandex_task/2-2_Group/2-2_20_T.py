# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

first_str = input()
second_str = input()
third_str = input()

target_string = "зайка"

is_present_in_first_str = target_string in first_str
is_present_in_second_str = target_string in second_str
is_present_in_third_str = target_string in third_str

result_for_print = None
lenn = None

if is_present_in_first_str:
    if is_present_in_second_str and is_present_in_third_str:
        result_for_print = min(first_str, second_str, third_str)
        lenn = len(result_for_print)
    elif is_present_in_second_str:
        result_for_print = min(first_str, second_str)
        lenn = len(result_for_print)
    elif is_present_in_third_str:
        result_for_print = min(first_str, third_str)
        lenn = len(result_for_print)
    else:
        result_for_print = first_str
        lenn = len(result_for_print)
else:
    if is_present_in_second_str and is_present_in_third_str:
        result_for_print = min(second_str, third_str)
        lenn = len(result_for_print)
    elif is_present_in_second_str:
        result_for_print = second_str
        lenn = len(result_for_print)
    elif is_present_in_third_str:
        result_for_print = third_str
        lenn = len(result_for_print)


if result_for_print is not None:
    print(f"{result_for_print} {lenn}")


"""
Зайка — 2
По пути домой родители вновь решили сыграть с детьми в поиск зверушек.

Формат ввода
Три строки описывающих придорожную местность.

Формат вывода
Строка в которой есть зайка, а затем её длина.
Если таких строк несколько, выбрать ту, что меньше всех лексикографически.

Пример 1
    Ввод
        березка елочка зайка волк березка
        сосна сосна сосна елочка грибочки медведь
        сосна сосна сосна белочка сосна белочка
    Вывод
        березка елочка зайка волк березка 33
        
Пример 2
    Ввод
        зайка березка
        березка зайка
        березка елочка березка
    Вывод
        березка зайка 13
"""
