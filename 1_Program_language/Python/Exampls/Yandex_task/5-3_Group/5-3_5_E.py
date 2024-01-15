import traceback


def merge(tuple_1, tuple_2):
    checker(tuple_1, tuple_2)
    targetList = list()
    targetList += list(tuple_1)
    targetList += list(tuple_2)
    targetList.sort() # Вот чего не хватало. На чем падал на 6ом шаге. ### 	Ответ неверен (WA)
    return tuple(targetList)


def checker(tuple_1, tuple_2):
    checkIsIterable(tuple_1)
    checkIsIterable(tuple_2)
    checkIsSameType(tuple_1, tuple_2)
    checkIsSorted(tuple_1)
    checkIsSorted(tuple_2)


def checkIsIterable(targetOject):
    was_raised_exception = False
    try:
        iter(targetOject)
    except Exception:
        was_raised_exception = True
    if was_raised_exception:
        raise StopIteration()


def checkIsSameType(aFirstIter, aSecondIter):
    if not (type(aFirstIter) is type(aSecondIter)):
        raise TypeError()
    setOfType = set()
    for i in aFirstIter:
        setOfType.add(type(i))
    for k in aSecondIter:
        setOfType.add(type(k))
    if len(setOfType) > 1:
        raise TypeError()


def checkIsSorted(targetObject):
    sortedList = list(targetObject)
    sortedList.sort()

    rowList = list(targetObject)
    if sortedList != rowList:
        raise ValueError()


def old_checkIsSameType(aFirstIter, aSecondIter):
    first = iter(list(aFirstIter))
    second = iter(list(aSecondIter))
    if not (type(next(first)) is type(next(second))):
        raise TypeError()


def old_checkIsSameTypeEachElements(targetOject):
    sett = set()
    for i in targetOject:
        sett.add(type(i))
    if len(sett) > 1:
        raise TypeError()


try:
    print(*merge(35, (1, 2, 3)))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge("35", ("1", "2", "3")))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge("53", ("1", "2", "3")))
except Exception as e:
    traceback.print_exception(e, limit=0)
# Вопрос....
try:
    print(*merge("35", (1, 2, 3)))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge("335", ("a", "b", "c")))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge([3, 2, 1], range(10)))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge(["a", "b"], range(10)))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge([1.0, 2.0], [4.0, 5.0]))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge([1.0, 1.0], [4.0, 5.0]))
except Exception as e:
    traceback.print_exception(e, limit=0)

try:
    print(*merge(range(23, 55, 2), range(10)))
except Exception as e:
    traceback.print_exception(e, limit=0)
"""
см. 4-3_6_F.py и 4-1_10_J.py - везде идёт сортировка.


Слияние с проверкой
Когда-то вы уже писали функцию merge, которая производит слияние двух отсортированных кортежей.

Давай-те её немного переработаем.

Введём систему проверок:

если один из параметров не является итерируемым объектом, то вызовите исключение StopIteration;
если значения входных параметров содержат «неоднородные» данные, то вызовите исключение TypeError;
если один из параметров не отсортирован, то вызовите исключение ValueError.
Проверки следует проводить в указанном порядке.

Если параметры прошли все проверки, верните итерируемый объект, являющийся слиянием двух переданных.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(*merge(35, (1, 2, 3)))
Вывод
    Вызвано исключение StopIteration
Пример 2
Ввод
    print(*merge([3, 2, 1], range(10)))
Вывод
    Вызвано исключение ValueError
"""
