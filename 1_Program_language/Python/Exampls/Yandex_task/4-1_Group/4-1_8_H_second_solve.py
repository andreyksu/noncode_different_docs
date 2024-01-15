def is_palindrome(target):
    if isinstance(target, int):
        resultt = doWorkWithInt(target)
    elif isinstance(target, str):
        resultt = doWorkWithStr(target)
    elif isinstance(target, tuple):
        resultt = doWorkWithStr(target)
    elif isinstance(target, list):
        resultt = doWorkWithList(target)
    else:
        print("Missed target type")
    return resultt


def doWorkWithList(target):
    return verify(target)


def doWorkWithStr(target):
    return verify(list(target))


def doWorkWithTypel(target):
    return verify(list(target))


def doWorkWithInt(target):
    listt = list(str(target))
    return verify(listt)


def verify(listt):
    listt = [str(i).lower() for i in listt]
    listt_1 = listt[::-1]
    if listt == listt_1:
        return True
    else:
        return False


print("int-----" * 5)
print(is_palindrome(123))
print(is_palindrome(1))
print("str-----" * 5)
print(is_palindrome(""))
print(is_palindrome("dddddddddddddddddddddddddddd"))
print(is_palindrome("1w2W1"))
print(is_palindrome("1ww1"))
print(is_palindrome("1ww11"))
print("list-----" * 5)
print(is_palindrome([1, 2, 1, 2, 1]))
print(is_palindrome([1, 2, 1, 2, 2]))
print("tuple-----" * 5)
print(is_palindrome((1, 2, 1, 2, 1)))
print(is_palindrome((1, 2, 1, 2, 2)))
print(is_palindrome((1)))
print(is_palindrome(()))
