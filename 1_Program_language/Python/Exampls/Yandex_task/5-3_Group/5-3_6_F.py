class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


# a*x**2 + b*x + c = 0
def find_roots(a, b, c):
    D = b * b - 4 * a * c    
    if D < 0 or (a == b == 0 and c != 0):
        # print("No solution")
        raise NoSolutionsError()
    elif a == 0 and b == 0 and c == 0:
        # print("Infinite solutions")
        raise InfiniteSolutionsError()
    elif a == 0 and b != 0:
        x1 = -c / b
        x1 = float(x1)
        if x1 == 0:
            # print("0")
            return (x1, x1)
        else:
            # print(f"{x1:.2f}")
            return (x1, x1)
    else:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        x1 = float(x1)
        x2 = float(x2)
        minn = min(x1, x2)
        maxx = max(x1, x2)
        if minn == maxx:
            # print(f"{min:.2f}")
            return (minn, minn)
        else:
            # print(f"{min:.2f} {max:.2f}")
            return (minn, maxx)


# print(find_roots(0, 0, 1))
print(find_roots(1, 2, 1))
print(find_roots(0, 2, 1))

"""
см. 2-2_17_Q.py

Корень зла 2
В одной из первых лекций вы уже решали задачу о поиске корней уравнения. Давайте модернизируем её.

Напишите функцию find_roots, принимающую три параметра: коэффициенты уравнения и возвращающую его корни в виде кортежа из двух значений.

Так же создайте два собственных исключения NoSolutionsError и InfiniteSolutionsError, которые будут вызваны в случае отсутствия и бесконечного количества решений уравнения соответственно.

Если переданные коэффициенты не являются рациональными числами, вызовите исключение TypeError.

####### А эту проверку я так и не сделал.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(find_roots(0, 0, 1))
Вывод
    Вызвано исключение NoSolutionsError
Пример 2
Ввод
    print(find_roots(1, 2, 1))
Вывод
    (-1.0, -1.0)
"""
