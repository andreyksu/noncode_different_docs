from itertools import combinations, permutations, product

print(list(product([1, 2])))

print([(x, y) for x in [1, 2] for y in [3, 4]])
print([[(x, y) for x in [1, 2]] for y in [3, 4]])
print([(x, y) for x in [1, 2] for y in [3, 4]])

listt = [1, 2, 3, 4]
print(listt.pop())
print(listt)