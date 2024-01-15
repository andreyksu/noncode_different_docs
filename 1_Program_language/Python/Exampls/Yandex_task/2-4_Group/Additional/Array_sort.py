# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

# Сортировка массива/списка
listt = [1, 5, 5, 6, 7, 1, 2]

right_bound = len(listt) - 1

for i in range(0, right_bound):
    for j in range(0, right_bound - i):
        if listt[j] > listt[j + 1]:
            listt[j], listt[j + 1] = listt[j + 1], listt[j]

print(listt)
