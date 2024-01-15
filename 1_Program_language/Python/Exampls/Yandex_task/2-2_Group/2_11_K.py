# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

input_digital = int(input())

hundreds = input_digital // 100
tens = (input_digital % 100) // 10
units = input_digital % 10

sort_str = str(input_digital).sort()

max_num = max(hundreds, tens, units)
min_num = min(hundreds, tens, units)

# Это первое решение "не очень удачное" или точнее "Очень неудачное". В 2_14_task.py самое короткое решение.
# Разумеется еще проще отсортировать в коллекции и получить позиционно.

if max_num == hundreds:
    if min_num == tens:
        medium_num = units
    elif min_num == units:
        medium_num = tens
elif max_num == tens:
    if min_num == hundreds:
        medium_num = units
    elif min_num == units:
        medium_num = hundreds
elif max_num == units:
    if min_num == hundreds:
        medium_num = tens
    else:
        medium_num = hundreds    
#-----------------------------

# Это второе решение поиска среднего тоже не очень удачное. В 2_14_task.py самое короткое решение

medium_num = None

if hundreds == tens:
    medium_num = tens
elif hundreds == units:
    medium_num = units
elif tens == units:
    medium_num = units

if medium_num != None:  # Без этого предохранителя будет ошибка на 112 и 221 для medium
    # print(f'medium_num = {medium_num}')
    pass
elif max_num != hundreds and min_num != hundreds:
    medium_num = hundreds
elif max_num != tens and min_num != tens:
    medium_num = tens
else:
    medium_num = units

#-----------------------------

print(f"max_dig = {max_num}     medium_num = {medium_num}      min_dig = {min_num}")

summ_min_max = max_num + min_num

if summ_min_max == medium_num * 2:
    print("YES")
else:
    print("NO")

"""
Красота спасёт мир
Одно из древних поверий гласит, что трёхзначное число красиво, если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.

Напишите систему определяющую красоту числа.

Формат ввода
Одно трёхзначное число

Формат вывода
YES — если число красивое, иначе — NO

Пример 1
    Ввод
        123
    Вывод
        YES
Пример 2
    Ввод
        748
    Вывод
        NO
"""
