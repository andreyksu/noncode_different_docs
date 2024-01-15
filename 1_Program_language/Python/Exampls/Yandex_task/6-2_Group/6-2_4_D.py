import numpy as np
import pandas as pd

# Первый вариант решения. Делается через np.where.
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

    # Не понятно от куда берутся индексы в DataFrame кто их приносит.
    dff.reset_index(drop=True, inplace=True)
    return dff


def discount(aa_df):
    a_df = aa_df.copy()
    a_df["cost"] = np.where(a_df["number"] > 2, a_df["cost"] / 2, a_df["cost"])
    return a_df


products = ["bread", "milk", "soda", "cream"]
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)


"""
Акция

Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:

При покупке больше двух товаров — скидка 50%

мелкий шрифт: скидка распространяется только на товары купленные в количестве более двух штук

Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую новый с учётом акции.
Примечание

Не удаляйте функцию cheque, она потребуется для тестирования.

Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.
Пример
Ввод

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)

Вывод

  product  price  number  cost
0   cream     72       1    72
1    milk     58       2   116
2    soda     99       3   297
  product  price  number   cost
0   cream     72       1   72.0
1    milk     58       2  116.0
2    soda     99       3  148.5

"""
