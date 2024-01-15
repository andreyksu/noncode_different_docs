import re

chk_name = re.compile(r"[^A-Za-zs]")

print(chk_name.search("ddd.aaaaa"))