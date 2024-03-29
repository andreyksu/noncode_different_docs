# numbers = [1, 2, 3, 4, 5]

# strr = set([x for x in numbers if (str(x**0.5).split(".")[-1] == "0")])
# strr = set([x for x in numbers if ((x**0.5) // 1 == x**0.5)])

# print(strr)

set([x for x in numbers if ((x**0.5) // 1 == x**0.5)])

'''
Множество всех полных квадратов
Полным квадратом назовём натуральное число, которое является квадратом другого натурального числа. Например: 1, 25, 144.

Вашему решению будет предоставлен список numbers, содержащий натуральные числа.

Разработайте выражение для генерации множества всех чисел, которые выступают полными квадратами.

Примечание
В решении не должно быть ничего, кроме выражения.

Пример 1
Ввод
numbers = [1, 2, 3, 4, 5]
Вывод
{1, 4}

Пример 2
Ввод
numbers = [number for number in range(16, 100, 4)]
Вывод
{16, 64, 36}
'''