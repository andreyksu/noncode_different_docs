class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            first, second = args[0].split("/")
            self._number = int(first)
            self._delimeter = int(second)
        else:
            self._number = args[0]
            self._delimeter = args[1]
        self.__reduction()

    def numerator(self, a_number=None):
        if a_number is None:
            return abs(self._number)
        else:
            if self._number * a_number < 0:
                self._number = abs(a_number) * (-1)
            else:
                self._number = abs(a_number)
            self.__reduction()

    def denominator(self, a_delimeter=None):
        if a_delimeter is None:
            return abs(self._delimeter)
        else:
            self._delimeter = a_delimeter
            self.__reduction()

    def __workWithSign(self):
        if self._delimeter < 0:
            self._delimeter = self._delimeter * (-1)
            self._number = self._number * (-1)

    def __reduction(self):
        self.__workWithSign()
        for i in range(abs(self._number), 1, -1):
            if self._number % i == 0 and self._delimeter % i == 0:
                self._number = self._number // i
                self._delimeter = self._delimeter // i
                break

    def __str__(self):
        return f"{self._number}/{self._delimeter}"

    def __repr__(self):
        return f"Fraction('{self._number}/{self._delimeter}')"

    def __neg__(self):
        tmp_number = self._number
        tmp_delimeter = self._delimeter
        return Fraction(tmp_number * (-1), tmp_delimeter)


# --------------------------------------------------
a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
e = Fraction(96, -60)
print(a, b, c, d, e)
print(*map(repr, (a, b, c, d, e)))
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction("-1/2")
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
a = Fraction(4, -6)
print(a, repr(a))
a.numerator(-4)
print(a, repr(a))


"""
Дроби v0.2
Продолжим разработку класса Fraction, который реализует предлагаемые дроби.

Предусмотрите возможность задать отрицательные числитель и/или знаменатель. А также перепишите методы __str__ и __repr__ таким образом, чтобы информация об объекте согласовывалась с инициализацией строкой.

Далее реализуйте оператор математического отрицания — унарный минус.

Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    a = Fraction(1, 3)
    b = Fraction(-2, -6)
    c = Fraction(-3, 9)
    d = Fraction(4, -12)
    print(a, b, c, d)
    print(*map(repr, (a, b, c, d)))
Вывод
    1/3 1/3 -1/3 -1/3
    Fraction('1/3') Fraction('1/3') Fraction('-1/3') Fraction('-1/3')
Пример 2
Ввод
    a = Fraction('-1/2')
    b = -a
    print(a, b, a is b)
    b.numerator(-b.numerator())
    a.denominator(-3)
    print(a, b)
    print(a.numerator(), a.denominator())
    print(b.numerator(), b.denominator())
Вывод
    -1/2 1/2 False
    1/3 -1/2
    1 3
    1 2
"""
