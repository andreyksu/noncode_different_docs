count_of_children = int(input())

dict_of_preference = dict()

for i in range(count_of_children):
    readed_str = input()
    name, porege = readed_str.split()
    if porege not in dict_of_preference:
        dict_of_preference[porege] = [name]
    else:
        tmp_list = dict_of_preference[porege]
        tmp_list.append(name)


target_parege = input()

if target_parege in dict_of_preference:
    list_of_chld = dict_of_preference[target_parege]
    list_of_chld.sort()
    for i in list_of_chld:
        print(i)
else:
    print("Таких нет")
