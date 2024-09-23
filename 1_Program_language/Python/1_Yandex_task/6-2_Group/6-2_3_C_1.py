import numpy as np
import pandas as pd


# Второй вариант решения.
# Первый не понравился в необходимости формировании 4х словарей.
def cheque(a_price_series, **kwargs):
    costDict = dict()

    sortedOrderSeries = pd.Series(kwargs)
    sortedOrderSeries.sort_index(inplace=True)
    # targetSeries = orderSeries if orderSeries.size > a_series.size else a_series
    targetSeries = sortedOrderSeries
    for productName in targetSeries.keys():
        try:
            amount = sortedOrderSeries[productName]
            price = a_price_series[productName]
            cost = amount * price
        except Exception:
            continue
        costTargetProduct = costDict.get(productName, 0)
        costTargetProduct = costTargetProduct + cost
        costDict[productName] = costTargetProduct

    dff = pd.DataFrame(
        {
            "product": costDict.keys(),
            "price": a_price_series[costDict.keys()],
            "number": sortedOrderSeries[costDict.keys()],
        }
    )
    dff["cost"] = dff["price"] * dff["number"]

    # Не понятно от куда берутся индексы в DataFrame кто их приносит. Приходится сбрасывать.
    dff.reset_index(drop=True, inplace=True)
    return dff


products = ["bread", "milk", "soda", "cream"]
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1, cream1=1, cream2=2)
print(result)


"""
Чек - 2

В местном магазине решили добавить анализ данных и каждый чек представлять в виде DataFrame.
Прайс-лист уже сформирован в виде объекта Series, где индексами являются названия, а значениями — цены.

Напишите функцию, cheque, которая принимает прайс-лист и список покупок в виде неопределённого количества именованных параметров (ключ — название товара, значение — количество).

Функция должна вернуть объект DataFrame со столбцами:

    наименование продукта (product);
    цена за единицу (price);
    количество (number);
    итоговая цена (cost).

Строки чека должны быть отсортированы по названию продуктов в лексикографическом порядке.
Примечание

Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.
Пример
Ввод

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)

Вывод

  product  price  number  cost
0   cream     72       1    72
1    milk     58       2   116
2    soda     99       3   297

"""
