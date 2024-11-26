listt = list()
accurace = 2


def enter_results(*args):
    global listt
    listt = listt + list(args)


def get_sum():
    first_sum = 0
    second_sum = 0
    for i in range(len(listt)):
        if (i + 1) % 2 == 0:
            second_sum += listt[i]
        else:
            first_sum += listt[i]
    return (roundd(first_sum), roundd(second_sum))


def get_average():
    half = len(listt) // 2
    first, second = get_sum()
    return (roundd(first / half), roundd(second / half))


def roundd(target_num):
    res_num = (
        int(target_num) if isinstance(target_num, int) else round(target_num, accurace)
    )
    return res_num


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
"""
enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
"""


"""
В эфире рубрика «Эксперименты»
Лаборанты проводят эксперимент и запросили разработку системы обработки данных. Результатами эксперимента должны стать пары рациональных чисел.

Для работы им требуются функции:

enter_results(first, second, ...) — добавление данных одного или нескольких результатов (гарантируется, что количество параметров будет чётным);
get_sum() — возвращает пару сумм результатов экспериментов;
get_average() — возвращает пару средних арифметических значений результатов экспериментов.
Все вычисления производятся с точностью до сотых.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
Вывод
(9, 12) (3.0, 4.0)
(10, 14) (2.5, 3.5)
Пример 2
Ввод
enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
Вывод
(48.7, 40.13) (24.35, 20.07)
(53.9, 47.43) (17.97, 15.81)
(58.27, 54.7) (9.71, 9.12)
"""