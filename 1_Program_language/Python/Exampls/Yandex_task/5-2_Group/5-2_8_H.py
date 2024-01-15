import time
import math


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            first, second = args[0].split("/")
            self.__number = int(first)
            self.__delimeter = int(second)
        else:
            self.__number = args[0]
            self.__delimeter = args[1]
        self.__reduction()

    def numerator(self, a_number=None, hide_sign=True):
        if a_number is None:
            if hide_sign:
                return abs(self.__number)
            else:
                return self.__number
        else:
            if self.__number * a_number < 0:
                self.__number = abs(a_number) * (-1)
            else:
                self.__number = abs(a_number)
            self.__reduction()

    def denominator(self, a_delimeter=None):
        if a_delimeter is None:
            return abs(self.__delimeter)
        else:
            self.__delimeter = a_delimeter
            self.__reduction()

    def reverse(self):
        self.__number, self.__delimeter = self.__delimeter, self.__number
        return Fraction(self.__number, self.__delimeter)

    def __workWithSign(self):
        if self.__delimeter < 0:
            self.__delimeter = self.__delimeter * (-1)
            self.__number = self.__number * (-1)

    def __reduction(self):
        self.__workWithSign()
        # Заменил на эту часть и стало всё считаться мгновенно.
        k = math.gcd(self.__number, self.__delimeter)
        self.__number = self.__number // k
        self.__delimeter = self.__delimeter // k

    def __str__(self):
        return f"{self.__number}/{self.__delimeter}"

    def __repr__(self):
        return f"Fraction('{self.__number}/{self.__delimeter}')"

    def __neg__(self):
        tmp_number = self.__number
        tmp_delimeter = self.__delimeter
        return Fraction(tmp_number * (-1), tmp_delimeter)

    def __get_agreement_val(self, other):
        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = other.numerator(None, False)
        other_delimeter = other.denominator()

        current_number_agreement = current_number * other_delimeter
        current_delimeter_agreement = current_delimeter * other_delimeter

        other_number_agreement = other_number * current_delimeter
        other_delimeter_agreement = other_delimeter * current_delimeter

        return (
            (current_number_agreement, current_delimeter_agreement),
            (other_number_agreement, other_delimeter_agreement),
        )

    def __lt__(self, a_other):
        """<"""
        current, other = self.__get_agreement_val(a_other)
        return current[0] < other[0]

    def __le__(self, a_other):
        """<="""
        current, other = self.__get_agreement_val(a_other)
        return current[0] <= other[0]

    def __eq__(self, a_other):
        """=="""
        current, other = self.__get_agreement_val(a_other)
        return current[0] == other[0]

    def __ne__(self, a_other):
        """!="""
        current, other = self.__get_agreement_val(a_other)
        return current[0] != other[0]

    def __gt__(self, a_other):
        """>"""
        current, other = self.__get_agreement_val(a_other)
        return current[0] > other[0]

    def __ge__(self, a_other):
        """>="""
        current, other = self.__get_agreement_val(a_other)
        return current[0] >= other[0]

    def __iadd__(self, a_other):
        """self += other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] + other[0]
        summ_of_del = current[1]
        self.__number = summ_of_num
        self.__delimeter = summ_of_del
        self.__reduction()
        return self

    def __isub__(self, a_other):
        """self -= other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] - other[0]
        summ_of_del = current[1]
        self.__number = summ_of_num
        self.__delimeter = summ_of_del
        self.__reduction()
        return self

    def __add__(self, a_other):
        """self + other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] + other[0]
        summ_of_del = current[1]
        return Fraction(summ_of_num, summ_of_del)

    def __sub__(self, a_other):
        """self - other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] - other[0]
        summ_of_del = current[1]
        return Fraction(summ_of_num, summ_of_del)

    def __mul__(self, a_other):
        """self * other"""
        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        return Fraction(
            current_number * other_number, current_delimeter * other_delimeter
        )

    def __truediv__(self, a_other):
        """self / other"""
        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        return Fraction(
            current_number * other_delimeter, current_delimeter * other_number
        )

    def __imul__(self, a_other):
        """self *= other"""
        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        self.__number = current_number * other_number
        self.__delimeter = current_delimeter * other_delimeter
        self.__reduction()
        return self

    def __itruediv__(self, a_other):
        """self /= other"""
        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        self.__number = current_number * other_delimeter
        self.__delimeter = current_delimeter * other_number
        self.__reduction()
        return self


# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
start_time = time.time()
a = Fraction(20000000, 300000000000001)
b = Fraction(1, 20000)
c = a + b + b + b + b + b + b + b + b + b + b + b + b + b + b
print(c)

print("--- %s seconds ---" % (time.time() - start_time))
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(1, 3)
b = Fraction(1, 2)
c = a * b
print(a, b, c, a is c, b is c)
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(1, 3)
c = b = Fraction(2, 1).reverse()
b /= a
print(a, b, c, b is c)
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(1, 3)
b = Fraction(1, 2)
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(1, 3)
b = Fraction(6, 2).reverse()
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

"""
Дроби v0.5
Следующим этапом разработки будет реализация методов сравнения: >, <, >=, <=, ==, !=.

Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
Вывод
    False True False True False False
Пример 2
Ввод
    a = Fraction(1, 3)
    b = Fraction(6, 2).reverse()
    print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
Вывод
    False False True True True True
"""
