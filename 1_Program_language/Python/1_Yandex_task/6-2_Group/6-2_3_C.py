import numpy as np
import pandas as pd

# Первый вариант решения. Не нравится что приходится формировать 4ре словаря.
# Но это решение прошло проверки.
def cheque(a_series, **kwargs):
    costDict = dict()
    resultDict = dict()

    sortedOrderSeries = pd.Series(kwargs)
    sortedOrderSeries.sort_index(inplace=True)
    # targetSeries = orderSeries if orderSeries.size > a_series.size else a_series
    targetSeries = sortedOrderSeries
    for productName in targetSeries.keys():
        try:
            amount = sortedOrderSeries[productName]
            price = a_series[productName]
            cost = amount * price
        except Exception:
            continue
        # Это можно удалить, по сути это не нужно. Чисто теоретически, может пригодиться при дублирующих ключах.
        # Но видимо нельзя передать два одноимённых параметров в функцию. Да и для словаря это не возможно, чтоб два одинаковых ключа.
        # А если предположить что мы так получим из вне. То сначала одноименные(для одного товара) amount просуммировать, после чего переходить к подсчёту.
        costTargetProduct = costDict.get(productName, 0)
        costTargetProduct = costTargetProduct + cost
        costDict[productName] = costTargetProduct

        # Эта часть мне не нравится. Не нравится необходимость в наполнении четырёх листов в dict.
        targettProd = resultDict.get("product", [])
        targettProd.append(productName)
        resultDict["product"] = targettProd

        targettPrice = resultDict.get("price", [])
        targettPrice.append(price)
        resultDict["price"] = targettPrice

        # Cost - мы суммируем, если для одного товара будет переданно два одноименных именованных параметров.
        # А вот само количество amount, заданное в именнованных параметрах не суммируется и будет выыедено последнее.
        targettNumber = resultDict.get("number", [])
        targettNumber.append(amount)
        resultDict["number"] = targettNumber

        targettCost = resultDict.get("cost", [])
        targettCost.append(cost)
        resultDict["cost"] = targettCost

    return pd.DataFrame(resultDict)


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
