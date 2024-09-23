strr = "a&nbsp;&nbsp;&nbsp;&nbsp;b\n\nd\nl"

intermediate = strr.replace("&nbsp;", " ").replace("\n", " ")
print(intermediate)

new_strr = [x for x in intermediate if x != " "]
print(new_strr)