list_of_pair = list()
resut_set = set()
dictt = dict()

while (readed_str := input()) != "":
    tmp_list = readed_str.split()
    list_of_pair.append(tmp_list)
    for target_person in tmp_list:
        resut_set.add(target_person)

result_list = list(resut_set)
result_list.sort()


for target_person in result_list:
    for upp_pair in list_of_pair:
        if target_person in upp_pair:
            position = upp_pair.index(target_person)
            friend = upp_pair[position - 1]
            print(f"i = {target_person} ---- friedn = {friend}")
            for sub_pair in list_of_pair:
                if friend in sub_pair:
                    sub_position = sub_pair.index(friend)
                    sub_friend = sub_pair[sub_position - 1]
                    if target_person == sub_friend:
                        print("target_person == sub_friend")
                        continue
                    print(f"friedn = {friend} ---- sub_friedn = {sub_friend}")
                if target_person in dictt:
                    print(f"dictt[target_person].add(sub_friend) :::: {target_person} :::: {sub_friend}")
                    dictt[target_person].add(sub_friend)
                else:
                    print(f"dictt[target_person] = sub_friend :::: {target_person} :::: {sub_friend}")
                    dictt[target_person] = {sub_friend}

print()

for i in dictt:
    print(i, dictt[i])
