from itertools import combinations, permutations, product

# !NB решение на нравится.
# 1. Изначально писал без методов(по материалу их еще не давали), лишь потом добавил методы по этой причине не очень складно. Лишние вызовы или обращение к глобальным переменным.
# 2. Сами методе не очень продуманы. Достаточно неуклюжим и большим является метод разбора в польскую запись, да и остальные тоже не очень удачные.

# src_str = "A or C ~ not (A -> B) or C and ( A and B not C)"
# src_str = "A or C ~ not (A -> B) or C and ( A and B not C ~ A)"
src_str = input()

# Дефолтные значения.
BINARY_LIST = [0, 1]
OPERATIONS = ["not", "and", "or", "^", "->", "~"]
OPERATIONS_REPLACE = {
    "not": "not",
    "and": "and",
    "or": "or",
    "^": "!=",
    "->": "<=",
    "~": "==",
}
BRACES = ["(", ")"]


def fetchVariables(a_str):
    """
    Выбирае все буквы в верхнем регистре из исходного выражения.
    """
    setOfVar = set()
    for i in a_str:
        if i.isalpha() and i.isupper():
            setOfVar.add(i)
    listtOfVar = list(setOfVar)
    listtOfVar.sort()
    return listtOfVar


def peareListToPolishOperateFromString(a_row_str):
    """
    Добавляем пробелы между ивестными элементами для последующего разделения.
    """
    extended_list = list()
    extended_list.extend(OPERATIONS)
    extended_list.extend(BRACES)
    extended_list.extend(fetchVariables(a_row_str))
    # Т.к. строка то её изменние не влияет на исходную.
    for i in extended_list:
        a_row_str = a_row_str.replace(i, f" {i}  ")

    # Непосредственно разделение по пробелам.
    # splited_src_str = a_row_str.split(" ")
    splited_src_str = a_row_str.split() # Если без указания разделителя, то пустые строки отсутствуют.
    # newList = list()
    # for i, elem in enumerate(splited_src_str):
    #    if elem != "":
    #        newList.append(elem)
    # return newList
    return splited_src_str


def doPolishString(a_str):
    """
    Формирует польскую обратную запись
    """
    prepared_str = peareListToPolishOperateFromString(a_str)
    stack = list()
    result_pol = list()

    for i in prepared_str:
        if i in OPERATIONS:
            while len(stack) > 0: # while stack: Можно так.
                elemFomStack = stack.pop()
                if (elemFomStack in OPERATIONS) and (
                    OPERATIONS.index(elemFomStack) <= OPERATIONS.index(i)
                ):
                    result_pol.append(elemFomStack)
                else:
                    stack.append(elemFomStack)
                    stack.append(i)
                    break
            else:
                stack.append(i)
        elif i == BRACES[0]:
            stack.append(i)
        elif i == BRACES[1]:
            while len(stack) > 0: # while stack: Можно так.
                open = stack.pop()
                if open in BRACES:
                    break
                result_pol.append(open)
        else:
            result_pol.append(i)

    while len(stack) > 0: # while stack: Можно так.
        elem = stack.pop()
        result_pol.append(elem)

    return result_pol


def calcExpression(a_result_pol, a_dict_to_eval):
    """
    Выполняет непосредственное вычисление (оценку выражений через eval)
    """
    list_as_stack = list()
    result = 0
    for item in a_result_pol:
        if item not in OPERATIONS:
            list_as_stack.append(item)
        elif item == OPERATIONS[0]:
            first = list_as_stack.pop()
            result = eval(f"{OPERATIONS[0]} {first}", a_dict_to_eval)
            list_as_stack.append(result)
        else:
            second = list_as_stack.pop()
            first = list_as_stack.pop()
            oper = OPERATIONS_REPLACE[item]
            result = eval(f"{first} {oper} {second}", a_dict_to_eval)
            list_as_stack.append(result)
    return int(list_as_stack[0])


# -----------------------------------
def getProduct(a_src_str):
    str_for_product = ""
    for _ in range(len(fetchVariables(a_src_str)) - 1):
        str_for_product += "BINARY_LIST, "
    else:
        str_for_product += "BINARY_LIST"
    str_for_product_eval = "product(" + str_for_product + ")"
    # Все это безобразие нужно было убрать и сделать так list(product([0, 1], repeat=len(fetchVariables(a_src_str))))
    resultOfEvaluateProduct = eval(str_for_product_eval)
    return resultOfEvaluateProduct


# Выводит заголовок
for charr in fetchVariables(src_str):
    print(charr, end=" ")
print("F")

polishStr = doPolishString(src_str)
# Выводит саму таблицу
for concrete_product in getProduct(src_str):
    dict_to_eval = dict()
    for position, targ_char in enumerate(fetchVariables(src_str)):
        dict_to_eval[targ_char] = concrete_product[position]
    resul_of_eval = calcExpression(polishStr, dict_to_eval)
    for val_in_product in concrete_product:
        print(val_in_product, end=" ")
    print(int(resul_of_eval))


"""
Таблицы истинности 3
Продолжим работу с таблицами истинности.
К сожалению, некоторые из операций Булевой алгебры не реализованы в Python.
Самые частые не стандартные операции это: импликация, строгая дизъюнкция и эквивалентность.

Обозначим их следующим образом:

импликация — ->;
строгая дизъюнкция — ^;
эквивалентность — ~.
Напишите программу, которая для введённого сложного логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных.

Возможное содержание выражения:

Заглавная латинская буква — переменная;
not — отрицание;
and — конъюнкция;
or — дизъюнкция;
^ — строгая дизъюнкция;
-> — импликация;
~ — эквивалентность;
() — логические скобки.
Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
Прежде, чем реализовывать новые операции, обратите внимание на их приоритет.
Рекомендуем воспользоваться знаниями полученными при решении задачи «Польский калькулятор».

Пример 1
    Ввод
    A -> B ~ C
    Вывод
    A B C F
    0 0 0 0
    0 0 1 1
    0 1 0 0
    0 1 1 1
    1 0 0 1
    1 0 1 0
    1 1 0 0
    1 1 1 1

Пример 2
    Ввод
    A or C ~ not (A -> B) or C
    Вывод
    A B C F
    0 0 0 1
    0 0 1 1
    0 1 0 1
    0 1 1 1
    1 0 0 1
    1 0 1 1
    1 1 0 0
    1 1 1 1
"""
