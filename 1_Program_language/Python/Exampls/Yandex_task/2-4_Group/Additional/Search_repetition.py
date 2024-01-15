# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

# Происк повторений и вывод максимально, часто повторяющегося.
array = [1, 2, 3, 3, 2, 3, 4, 1, 2]

dictionary = dict()

for i in array:
    if i in dictionary.keys():
        print(i)
        tmpp = dictionary[i]
        dictionary[i] = tmpp + 1
    else:
        dictionary[i] = 1

print(dictionary)
print(dictionary.items())
print(dictionary.keys())

sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)
print(dict(sorted_dict))
