from itertools import combinations, permutations, product

try:
    f = open("234")
except FileNotFoundError as e:
    print("FileNotFoundError _ 1")
    print(e)
except Exception as e:
    print("Exception")
    print(e)
try:
    with open(
        "234"
    ) as file:  # Перехват ошибки на чтение есть, а вот перехват на ненайденный файл нет у with
        print(file)
except FileNotFoundError as e:
    print("FileNotFoundError _ 2")
    print(e)


print(not True or not False and not (False or True and not False))

# declaring an integer value
integer_val = 5

print(bin(integer_val))

aaaa = "abcd"
res = ""

for i in aaaa:
    res = i + res

print(res)


print(list(product([0, 1], repeat=3)))
