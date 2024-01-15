import time
import math


class Fraction:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            listt = args[0].split("/")
            if len(listt) == 1:
                self.__number = int(listt[0])
                self.__delimeter = int(1)
            else:
                self.__number = int(listt[0])
                self.__delimeter = int(listt[1])
        elif len(args) == 1 and isinstance(args[0], int):
            self.__number = args[0]
            self.__delimeter = 1
        else:
            self.__number = args[0]
            self.__delimeter = args[1]
        self.__reduction()

    def numerator(self, a_number=None, hide_sign=True):
        """
        Если hide_sign значение не задано, то возвращаем без знака. Как того требует правило вывода - беззнаковое значение.
        """
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
        """
        Разворачиваем/переворачиваем дробь.
        """
        self.__number, self.__delimeter = self.__delimeter, self.__number
        return Fraction(self.__number, self.__delimeter)

    def __workWithSign(self):
        """
        Приводит в порядок знаки.
        Если делитель задан как отрицательный, то перекидываем знак к числителю.
        Да и везде при выводе отражен знак у числителя.
        """
        if self.__delimeter < 0:
            self.__delimeter = self.__delimeter * (-1)
            self.__number = self.__number * (-1)

    def __reduction(self):
        """
        Производит сокращение дробей. Если это возможно.

        Заменил на эту часть 'math.gcd(...)' и стало всё считаться мгновенно.
        """
        self.__workWithSign()
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

    def __getFractionIfItIsnt(self, other):
        """
        Можно переделать в static метод.
        Если получили в other тип int - то оборачиваем его в Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other)
        return other

    def __get_agreement_val(self, other):
        """
        Приведение знаменателя к общему значению. Для сложения, вычтания, сравнения итд.
        """
        other = self.__getFractionIfItIsnt(other)

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

    def __gt__(self, a_other):
        """>"""
        current, other = self.__get_agreement_val(a_other)
        return current[0] > other[0]

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

    def __ge__(self, a_other):
        """>="""
        current, other = self.__get_agreement_val(a_other)
        return current[0] >= other[0]

    def __add__(self, a_other):
        """self + other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] + other[0]
        summ_of_del = current[1]
        return Fraction(summ_of_num, summ_of_del)

    def __radd__(self, other):
        """other + self"""
        return self.__add__(other)

    def __iadd__(self, a_other):
        """self += other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] + other[0]
        summ_of_del = current[1]
        self.__number = summ_of_num
        self.__delimeter = summ_of_del
        self.__reduction()
        return self

    def __sub__(self, a_other):
        """self - other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] - other[0]
        summ_of_del = current[1]
        return Fraction(summ_of_num, summ_of_del)

    def __rsub__(self, a_other):
        """other - self"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = other[0] - current[0]
        summ_of_del = current[1]
        return Fraction(summ_of_num, summ_of_del)

    def __isub__(self, a_other):
        """self -= other"""
        current, other = self.__get_agreement_val(a_other)
        summ_of_num = current[0] - other[0]
        summ_of_del = current[1]
        self.__number = summ_of_num
        self.__delimeter = summ_of_del
        self.__reduction()
        return self

    def __mul__(self, a_other):
        """self * other"""

        a_other = self.__getFractionIfItIsnt(a_other)

        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        return Fraction(
            current_number * other_number, current_delimeter * other_delimeter
        )

    def __rmul__(self, other):
        """other * self"""
        return self.__mul__(other)

    def __imul__(self, a_other):
        """self *= other"""
        a_other = self.__getFractionIfItIsnt(a_other)

        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        self.__number = current_number * other_number
        self.__delimeter = current_delimeter * other_delimeter
        self.__reduction()
        return self

    def __truediv__(self, a_other):
        """self / other"""
        a_other = self.__getFractionIfItIsnt(a_other)

        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        return Fraction(
            current_number * other_delimeter, current_delimeter * other_number
        )

    def __rtruediv__(self, a_other):
        """other / self"""
        a_other = self.__getFractionIfItIsnt(a_other)

        current_number = self.__number
        current_delimeter = self.__delimeter

        other_number = a_other.numerator(None, False)
        other_delimeter = a_other.denominator()

        return Fraction(
            other_number * current_delimeter, other_delimeter * current_number
        )

    def __itruediv__(self, a_other):
        """self /= other"""
        a_other = self.__getFractionIfItIsnt(a_other)

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
a = Fraction(1)
b = Fraction("2")
c, d = map(Fraction.reverse, (2 + a, -1 + b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(1, 2)
b = Fraction("2/3")
c, d = map(Fraction.reverse, (3 - a, 2 / b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)

"""
Дроби v0.7
"Остался последний штрих!" Правда звучит как издевательство?

Мы «научили» наши дроби работать с целыми числами и вот теперь надо провернуть обратное действие. Реализуйте функционал, который позволит производить все арифметические операции с дробями и числами, независимо от их положения (слева или справа) в операторе.

Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    a = Fraction(1)
    b = Fraction('2')
    c, d = map(Fraction.reverse, (2 + a, -1 + b))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)
Вывод
    1/1 2/1 1/3 1/1
    False False
    True True False True
Пример 2
Ввод
    a = Fraction(1, 2)
    b = Fraction('2/3')
    c, d = map(Fraction.reverse, (3 - a, 2 / b))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)
Вывод
    1/2 2/3 2/5 1/3
    False True
    False False False False
"""
