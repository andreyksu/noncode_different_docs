import os

user = os.getlogin()

strr = "/aaa/{0}/dddd"

print (strr.format(user))



listt_1 = [1, 2]
listt_2 = [3, 4]
listt_1.append(listt_2)
print (listt_1)