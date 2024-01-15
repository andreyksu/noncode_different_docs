 
class Fraction:
    """Два равных конструктора"""
    def __init1__(self, a_n=None, a_d=None):
        if isinstance(a_n, str) and a_d is None:
            first, second = a_n.split("/")
            self._number = int(first)
            self._delimeter = int(second)
        else:
            self._number = a_n
            self._delimeter = a_d
        self.__reduction()

    def __init__(self, *args):
        self.__isPositive = True
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
            return self._number
        else:
            self._number = a_number
            self.__reduction()

    def denominator(self, a_delimeter=None):
        if a_delimeter is None:
            return self._delimeter
        else:
            self._delimeter = a_delimeter
            self.__reduction()

    def __workWithSign(self):
        if (self._delimeter * self._number) > 0:
            self.__isPositive = self.__isPositive
        else:
            self.__isPositive = not self.__isPositive
        self._number = abs(self._number)
        self._delimeter = abs(self._delimeter)

    def __reduction(self):
        self.__workWithSign()
        for i in range(abs(self._number), 1, -1):
            if self._number % i == 0 and self._delimeter % i == 0:
                self._number = self._number // i
                self._delimeter = self._delimeter // i
                break

    def __getSing(self):
        sign = "" if self.__isPositive else "-"
        return sign

    def __str__(self):
        return f"{self.__getSing()}{self._number}/{self._delimeter}"

    def __repr__(self):
        return f"Fraction('{self.__getSing()}{self._number}/{self._delimeter}')"

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
kk = -b
numeratorkk = kk.numerator()
print(f"kk = {kk}, numeratorkk = {numeratorkk}")
b.numerator(-numeratorkk)
a.denominator(-3)
print(f"a = {a}, b = {b}")
a.denominator(-3)
b.numerator(-b.numerator())
print(f"a = {a}, b = {b}")
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
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
