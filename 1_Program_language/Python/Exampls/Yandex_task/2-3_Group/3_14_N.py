# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

# Этот работает для коря из целевого числа. Т.е. от 2 и до  N^1/2. Т.е. для 86 получаем [2, 7] от 2х до 7и. Таким образом сокращаем количество операций.
target_number = int(input())

target = int(target_number**0.5)

is_simple = True
if target_number == 1:
    is_simple = False
elif target_number <= 3:
    pass
else:
    for i in range(2, target + 1):
        if target_number % i == 0:
            is_simple = False
            break

if is_simple:
    print("YES")
else:
    print("NO")

"""
# Ошибка, долго считает.
target_number = int(input())

count = 0

for i in range(1, target_number + 1):
    if target_number % i == 0:
        count += 1

if count == 2:
    print("YES")
else:
    print("NO")
"""

"""
Простая задача
Один из самых интересных видов чисел в математике — простые числа. Их объединяет то, что делятся они лишь на 1 и само себя. До сих пор их изучают учёные по всему миру. Также они применяются в вычислительной технике: с их помощью можно писать алгоритмы, чтобы шифровать данные. Давайте напишем программу, чтобы определять — простое перед нами число или нет.

Формат ввода
Вводится одно натуральное число.

Формат вывода
Требуется вывести сообщение YES если число простое, иначе — NO.

Примечание
Простым называется число, которое имеет ровно два делителя.

Пример 1
    Ввод
        1
    Вывод
        NO
Пример 2
    Ввод
        67
    Вывод
        YES
"""
