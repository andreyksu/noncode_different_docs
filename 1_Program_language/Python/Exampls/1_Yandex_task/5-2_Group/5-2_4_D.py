class Fraction:
    def __init__(self, a_n=None, a_d=None):
        if isinstance(a_n, str) and a_d is None:
            first, second = a_n.split("/")
            self.number = int(first)
            self.delimeter = int(second)
        else:
            self.number = a_n
            self.delimeter = a_d
        self.__reduction()

    def numerator(self, a_number=None):
        if a_number is None:
            return self.number
        else:
            self.number = a_number
            self.__reduction()

    def denominator(self, a_delimeter=None):
        if a_delimeter is None:
            return self.delimeter
        else:
            self.delimeter = a_delimeter
            self.__reduction()

    def __reduction(self):
        for i in range(self(self.number), 1, -1):
            if self.number % i == 0 and self.delimeter % i == 0:
                self.number = self.number // i
                self.delimeter = self.delimeter // i
                break

    def __str__(self):
        return f"{self.number}/{self.delimeter}"

    def __repr__(self):
        return f"Fraction({self.number}, {self.delimeter})"


# --------------------------------------------------
fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction("7/14")
print(fraction, repr(fraction))
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction("7 /14")
print(fraction, repr(fraction))
# --------------------------------------------------
print("-" * 80)
# --------------------------------------------------
fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())


"""
Дроби v0.1
Возможно, вы уже заметили, что дробные числа (float) недостаточно точные для некоторых задач. Для более точных математических расчётов иногда прибегают к созданию правильных рациональных дробей, описываемых числителем и знаменателем.

Начнём разработку класса Fraction, который реализует предлагаемые дроби.

Предусмотрите возможность инициализации дроби с помощью двух целых чисел или строки в формате <числитель>/<знаменатель>.
В случаях наличия общего делителя у числителя и знаменателя, дробь следует сократить.

А также реализуйте методы:

numerator() — возвращает значение числителя;
numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
denominator() – возвращает значение знаменателя;
denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
__str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
__repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>).
Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все числа в данной задаче будут положительными.
Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    fraction = Fraction(3, 9)
    print(fraction, repr(fraction))
    fraction = Fraction('7/14')
    print(fraction, repr(fraction))
Вывод
    1/3 Fraction(1, 3)
    1/2 Fraction(1, 2)
Пример 2
Ввод
    fraction = Fraction(3, 210)
    print(fraction, repr(fraction))
    fraction.numerator(10)
    print(fraction.numerator(), fraction.denominator())
    fraction.denominator(2)
    print(fraction.numerator(), fraction.denominator())
Вывод
    1/70 Fraction(1, 70)
    1 7
    1 2
"""