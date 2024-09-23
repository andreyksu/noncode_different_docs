# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.

# ### Решение не нравится. 1. Конкатенация строк - это долго и ресурсно по памяти. 2. Сортировка прямая, обратная - а если данных много.
# Самое оптимальное решенать через Map<char, int> или через Set<char>
# Но еще можно через вложенные List где [[char, int], [char, int], ....] символ и его количество.


fuzze = "ФИНИШ"

tmp_list_of_str = list()

tmp_str = ""

while (target_str := input()) != fuzze:
    target_str = target_str.lower()
    tmp_str = tmp_str + target_str

tmp_list_of_str = list(tmp_str)
tmp_list_of_str.sort()
tmp_list_of_str.reverse()

count_char = 0
char = None

tmp_count = 0
tmp_char = None

# print(tmp_list_of_str)

for i in tmp_list_of_str:
    if str(i).isdigit() or str(i).isalpha():
        if tmp_char == i:
            tmp_count += 1
        else:
            if count_char <= tmp_count:
                count_char = tmp_count
                char = tmp_char
            tmp_char = i
            tmp_count = 1

print(char)
