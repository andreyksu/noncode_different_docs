import math

strr = input()

n, m = strr.split(" ")

N = int(n)
M = int(m)

common_result = math.comb(N, M)
# print(math.factorial(N) / (math.factorial(N - M) * math.factorial(M)))

targetResult = math.comb(N - 1, M - 1)

print(targetResult, common_result)


# print(math.perm(N, M))
# print(math.factorial(N) / math.factorial(N - M))

# print(math.perm(N))


"""
Есть варианты?
Вася пришёл на образовательный семинар и обнаружил, что зрителей на мероприятии — N, а количество мест — M.
Помогите Васе определить вероятность того, что он попадёт на семинар.

Формат ввода
Два числа 
N и M.

Формат вывода
Два числа — количество вариантов, в которых Вася попадает на семинар и количество всех вариантов групп на семинаре.

Примечание
В первом примере обозначим участников числами 1, 2, 3, 4. Предположим, что 1 — это Вася.

Тогда все вариации участников выглядят так:

    1 2
    1 3
    1 4
    2 3
    2 4
    3 4
А благополучными из них для Васи являются только 3:

    1 2
    1 3
    1 4

Пример 1
Ввод
    4 2
Вывод
    3 6
Пример 2
Ввод
    10 3
Вывод
    36 120
"""