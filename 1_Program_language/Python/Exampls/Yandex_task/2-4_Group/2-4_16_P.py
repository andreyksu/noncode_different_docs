# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

count = int(input())
width = int(input())

tire = count * width + (count - 1)

for i in range(1, count + 1):
    for j in range(1, count + 1):
        if j < count:
            endd = "|"
        else:
            endd = ""
        print(f"{i * j:^{width}}", end=endd)
    if i < count:
        print()
        print("-" * tire)

"""
Редизайн таблицы умножения
Согласитесь, что предыдущие таблицы умножения выглядят не очень красиво. Давайте зададим для всех столбцов одинаковую ширину, а значения в ячейках выровним по центру.
И да, заказчик попросил ещё добавить в таблицу рамки между ячейками.

Формат ввода
В первой строке записан требуемый размер таблицы. Во второй строке — ширина столбцов.

Формат вывода
Таблица умножения заданного размера и вида.

Пример 1
    Ввод
        3
        3
    Вывод
         1 | 2 | 3 
        -----------
         2 | 4 | 6 
        -----------
         3 | 6 | 9 
Пример 2
    Ввод
        5
        5
    Вывод
          1  |  2  |  3  |  4  |  5  
        -----------------------------
          2  |  4  |  6  |  8  | 10  
        -----------------------------
          3  |  6  |  9  | 12  | 15  
        -----------------------------
          4  |  8  | 12  | 16  | 20  
        -----------------------------
          5  | 10  | 15  | 20  | 25  
"""