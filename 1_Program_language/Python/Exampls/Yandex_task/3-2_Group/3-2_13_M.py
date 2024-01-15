input_count_of_dishes = int(input())

list_of_dishes = list()
sett_gotten_dishes = set()

for i in range(input_count_of_dishes):
    tmpp = input()
    list_of_dishes.append(tmpp)

list_of_dishes.sort()
count_of_blocks = int(input())

for ii in range(count_of_blocks):
    count_of_days = int(input())
    for iii in range(count_of_days):
        tmpp = input()
        sett_gotten_dishes.add(tmpp)

dictt = dict()
is_exist_free_dishes = False
for k in list_of_dishes:
    if k in sett_gotten_dishes:
        dictt[k] = True
    else:
        is_exist_free_dishes = True
        dictt[k] = False

if is_exist_free_dishes:
    for i in dictt:
        if not dictt[i]:
            print(i)
else:
    print("Готовить нечего")

"""
Дайте чего-нибудь новенького!
Главный повар детского сада хочет приготовить в праздничный день блюда, которые ни разу не готовил на этой неделе.
В его распоряжении есть список блюд:

которые можно приготовить в столовой сегодня;
которые были приготовлены в каждый из дней недели.
Формат ввода
Число блюд (N), которые можно приготовить в столовой.
N строк с названиями блюд. Число дней (M), о которых имеется информация. M блоков строк для каждого из списков. В первой строке каждого блока записано число блюд в заданный день, затем перечисляются эти блюда.

Формат вывода
Список блюд, которые ещё не готовились на этой неделе в алфавитном порядке.
Если все возможные блюда уже были приготовлены, следует вывести «Готовить нечего».

Пример
Ввод
5
Овсянка
Рис
Суп
Манная каша
Рыба
2
3
Рис
Суп
Рыба
2
Рис
Рыба
Вывод
Манная каша
Овсянка
"""