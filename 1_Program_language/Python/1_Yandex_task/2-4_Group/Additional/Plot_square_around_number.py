# ### - Означает(требуется оптимизация) - решение не очень нравится
# Решение не очень нравится. Как-то всё это сложно и повторяется много раз. Хотелось бы оптимизировать.

# Задача решена чуть чуть другая, в отличии от того что требовалось. В этом решении строится квадрат, относительно введенного числа. Введённое число в середине квадрата.

target = int(input())

side = ((target - 1) * 2) + 1

for i in range(1, target):
    k = 0
    for j in range(1, target):
        if k < i:
            k += 1
        print(k, end=" ")
    print(k, end=" ")
    for g in range(target, 1, -1):
        if g <= i:
            k -= 1
        print(k, end=" ")
    print()
# --------------- Это для нечетного куба. Средняя строка. А для четного она не нужна.
for i in range(1, target + 1):
    print(i, end=" ")
for i in range(target - 1, 0, -1):
    print(i, end=" ")
print()
# ---------------
for i in range(1, target):
    k = 0
    for j in range(1, target):
        if k < (target - i):
            k += 1
        print(k, end=" ")
    print(k, end=" ")
    for g in range(1, target):
        if g > i:
            k -= 1
        print(k, end=" ")
    print()

"""
Ввод
    3
Вывод:
    1 1 1 1 1 
    1 2 2 2 1 
    1 2 3 2 1 
    1 2 2 2 1 
    1 1 1 1 1
"""
