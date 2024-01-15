from sys import stdin

listt = list()

for line in stdin:
    tmp_str = line.rstrip("\n")
    listt += tmp_str.split()

newList = [int(x) for x in listt]

print(sum(newList))
    
"""
A+B+...
Наконец-то мы можем обрабатывать данные, не имея ни малейшего понятия об их количестве.

Напишите программу, которая находит сумму всех чисел введённых пользователем.

Формат ввода
Вводятся строки чисел.

Формат вывода
Одно число — сумма всех чисел в потоке ввода.

Пример
Ввод
1 2
3 4 5
6
7 8 9 10
Вывод
55
"""