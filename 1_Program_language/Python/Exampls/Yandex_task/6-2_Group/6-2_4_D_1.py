import numpy as np
import pandas as pd


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


# Оба варианта работает.
# Но при делении получаем float и на это ругается. Что несовметимые типы.
# По хорошему нужно изменить тип у столбца перед делением.
def discount(aa_df):
    a_df = aa_df.copy()
    # a_df["cost"].mask(a_df["number"] > 2, a_df["cost"] / 2, inplace=True)
    # Согласно интернету через loc самое быстрое.
    a_df.loc[a_df["number"] > 2, "cost"] = a_df['cost'] / 2
    # А это не рабочее. Тут в applay передаётся х т.е. значения number а значение cost не передаётся.Т.е. видимо испльзуется для одного столбца.
    # a_df["cost"] = a_df["number"].apply(lambda x: a_df["cost"] / 2 if x > 2 else a_df["cost"])
    # И так не работает.
    # a_df["cost"] = a_df["cost"].apply(lambda x: x / 2 if a_df["number"] > 2 else x)
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
