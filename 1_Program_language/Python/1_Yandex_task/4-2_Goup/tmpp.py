first = 1222222341234

print(first.bit_length())

print(bin(first))

mapp = {"ab": 1, "cb": 2, "cab": 3}

mask = "ab"

new_dict = dict()

for i in mapp:
    if mask in i:
        new_dict[i] = mapp[i]
        
print(new_dict)

diict = dict(filter(lambda kv: mask in kv[0], mapp.items()))
print(diict.get("cab"))

res = {kv[0]: kv[1] for kv in mapp.items() if mask in kv[0]}
print(res)


i = 0
marker = True

while marker:
    print(f'param') # Ну или что то другое. Может сложение чисел.
    if i < 26:
        i += 1
        marker = False