str1 = "hello"
str2 = "world"
#common_chars = [c1 + c2 for c1 in set(str1) for c2 in set(str2) if c1 == c2]
common_chars = [c1 + c2 for c1 in list(str1) for c2 in list(str2)]
print(common_chars)
