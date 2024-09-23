import time


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

    def __workWithSign(self):
        if self.__delimeter < 0:
            self.__delimeter = self.__delimeter * (-1)
            self.__number = self.__number * (-1)

    @staticmethod
    def __getListOfMultiplayers(targetNumber):
        listt = list()

        abs_number = abs(targetNumber)
        sqrtt_number = int(abs_number**1 / 2)
        if sqrtt_number < 2:
            return listt

        tmpp_numm = targetNumber
        for i in range(2, sqrtt_number + 1):
            while tmpp_numm % i == 0:
                tmpp_numm = tmpp_numm / i
                listt.append(i)

        return listt

    def __reduction(self):
        self.__workWithSign()
        listt = Fraction.__getListOfMultiplayers(self.__number)
        
        listt.append(self.__number)

        for i in listt:
            if self.__number % i == 0 and self.__delimeter % i == 0:
                self.__number = self.__number // i
                self.__delimeter = self.__delimeter // i

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



        listt_currentDelimeter = Fraction.__getListOfMultiplayers(current_delimeter)
        listt_otherDelimeter = Fraction.__getListOfMultiplayers(other_delimeter)
        # print(f'current_number = {current_number}, current_delimeter = {current_delimeter}, listt_currentDelimeter = {listt_currentDelimeter}')
        # print(f'other_number = {other_number}, other_delimeter = {other_delimeter}, listt_otherDelimeter = {listt_otherDelimeter}')        
        """
        Вообще нужно не так сделать. Нужно разложить на множитили эти делители.
        Найти различие между множествами этих коллекций множителей. И умножить на эти разницы.
        
        Разница для 
        
        a = Fraction(20000000, 3000000000000)
        b = Fraction(1, 20000)
        c = a + b + b + b + b + b + b + b + b + b + b + b + b
        
        --- 0.890106201171875 seconds --- с True
        --- 1.5059564113616943 seconds --- c False
        
        """        
        if len(listt_currentDelimeter) > 0 and len(listt_otherDelimeter) > 0 and False:
            tmpp_list = listt_currentDelimeter[:]
            for i in tmpp_list:
                if i in listt_otherDelimeter:
                    listt_otherDelimeter.remove(i)
                    listt_currentDelimeter.remove(i)

            # print(f'current_number = {current_number}, current_delimeter = {current_delimeter}, listt_currentDelimeter = {listt_currentDelimeter}')
            # print(f'other_number = {other_number}, other_delimeter = {other_delimeter}, listt_otherDelimeter = {listt_otherDelimeter}') 
            tmp_other_delimeter = 1
            for i in listt_otherDelimeter:
                tmp_other_delimeter *= i

            tmp_current_delimeter = 1
            for i in listt_currentDelimeter:
                tmp_current_delimeter *= i

            tmp_other_delimeter
            tmp_current_delimeter
            
            current_number_agreement = current_number * tmp_other_delimeter
            current_delimeter_agreement = current_delimeter * tmp_other_delimeter
            
            other_number_agreement = other_number * tmp_current_delimeter
            other_delimeter_agreement = other_delimeter * tmp_current_delimeter
            # print(f'current_number = {current_number}, current_delimeter = {current_delimeter}, listt_currentDelimeter = {listt_currentDelimeter}')
            # print(f'other_number = {other_number}, other_delimeter = {other_delimeter}, listt_otherDelimeter = {listt_otherDelimeter}') 
            
        else:
            current_number_agreement = current_number * other_delimeter
            current_delimeter_agreement = current_delimeter * other_delimeter

            other_number_agreement = other_number * current_delimeter
            other_delimeter_agreement = other_delimeter * current_delimeter
            
        # print(f'current_number_agreement = {current_number_agreement}, current_delimeter_agreement = {current_delimeter_agreement}')        
        # print(f'other_number_agreement = {other_number_agreement}, other_delimeter_agreement = {other_delimeter_agreement}')

        return (
            (current_number_agreement, current_delimeter_agreement),
            (other_number_agreement, other_delimeter_agreement),
        )

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


start_time = time.time()
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
a = Fraction(20000000, 3000000000000)
b = Fraction(1, 20000)
c = a + b + b + b + b + b + b + b + b + b + b + b + b
print(c)

print("--- %s seconds ---" % (time.time() - start_time))


"""
Дроби v0.3
Продолжим разработку класса Fraction, который реализует предлагаемые дроби.

Реализуйте бинарные операторы:

+ — сложение дробей, создаёт новую дробь;
- — вычитание дробей, создаёт новую дробь;
+= — сложение дробей, изменяет дробь, переданную слева;
-= — вычитание дробей, изменяет дробь, переданную слева.
Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    c = a + b
    print(a, b, c, a is c, b is c)
Вывод
    1/3 1/2 5/6 False False
Пример 2
Ввод
    a = Fraction(1, 8)
    c = b = Fraction(3, 8)
    b -= a
    print(a, b, c, b is c)
Вывод
    1/8 1/4 1/4 True
"""
