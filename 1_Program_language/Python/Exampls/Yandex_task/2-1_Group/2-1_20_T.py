# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

n = int(input())
m = int(input())
k_1 = int(input())
k_2 = int(input())

n_2 = (m * n - n * k_1) / (k_2 - k_1)
n_1 = (m * n - n_2 * k_2) / (k_1)

print(int(n_1), int(n_2))
