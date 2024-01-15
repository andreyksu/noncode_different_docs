# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.
# Это дополнение к 2_11_task.py третий способ поиска максимального, среднего, минимального, уже без встроенных функций.

number = 322

hundreds = number // 100
tens = (number % 100) // 10
units = number % 10

# Эти две цепочки условий - это то поиск максимального и минимального числа.
if hundreds >= tens and hundreds >= units:
    max = hundreds
elif tens >= hundreds and tens >= units:
    max = tens
else:
    max = units

if hundreds <= tens and hundreds <= units:
    min = hundreds
elif tens <= hundreds and tens <= units:
    min = tens
else:
    min = units

# Всё что снизу выполняется через сложение и вычитаение максимального и инимального из суммы.
if hundreds == tens or hundreds == units:
    medium = hundreds
elif tens == hundreds or tens == units:
    medium = tens
else:
    medium = None

if medium == None:
    if max - hundreds != 0 and min - hundreds != 0:
        medium = hundreds
    elif max - tens != 0 and min - tens != 0:
        medium = tens
    else:
        medium = units


print(f"max = {max}     mdedium = {medium}      min = {min}" )
