import numpy as np


# sizee = int(input())
def multiplication_matrix(sizee):
    aa = np.zeros((sizee, sizee), dtype="int32")

    for i in range(1, sizee + 1):
        a = np.arange(i, (sizee * i) + 1, i)
        aa[i - 1] = a

    # print(aa)
    return aa

print(multiplication_matrix(3))
print(multiplication_matrix(5))
print(multiplication_matrix(50))