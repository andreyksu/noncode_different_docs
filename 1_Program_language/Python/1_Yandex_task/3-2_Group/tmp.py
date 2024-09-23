listt = [(2, 1), (2, 2), (1, 2)]

dictt = dict()

if (1, 2) in listt:
    print("presetn")
    dictt[(1, 2)] = 1
    
print(dictt.get((1, 2)))