DICT = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ъ": "",
    "Ь": "",
}

lines = ""

# file_name_in = './Yandex_task/3-5_Group/3-5_6_F_cyrillic.txt'
file_name_in = "cyrillic.txt"
# file_name_out = './Yandex_task/3-5_Group/3-5_6_F_ transliteration.txt'
file_name_out = "transliteration.txt"

with open(file_name_in, "r", encoding="UTF-8") as file_in:
    lines = file_in.readlines()

for poss, i in enumerate(lines):
    for charr in DICT:
        if charr in i:
            i = i.replace(charr, DICT[charr].capitalize())
        if charr.lower() in i:
            i = i.replace(charr.lower(), DICT[charr].lower())
    lines[poss] = i

with open(file_name_out, "w", encoding="UTF-8") as file_out:
    file_out.writelines(lines)


"""
Транслитерация 2.0

Для международных документов русский текст преобразуется с использованием латинского алфавита. ГОСТ Р 52535.1-2006 задаёт правила транслитерации идентификационных карт.
Ниже приведена таблица замен:

А — A
Б — B
В — V
Г — G
Д — D
Е — E
Ё — E
Ж — ZH
З — Z
И — I
Й — I
К — K
Л — L
М — M
Н — N
О — O
П — P
Р — R
С — S
Т — T
У — U
Ф — F
Х — KH
Ц — TC
Ч — CH
Ш — SH
Щ — SHCH
Ы — Y
Э — E
Ю — IU
Я — IA
Давайте транслитерируем русский текст.
Букву «ё» транслитерируйте как «e», «й» как «и», а «ъ» и «ь» (и их заглавные версии «Ъ» и «Ь») должны исчезнуть из текста. Строчные буквы заменяются на строчные, заглавные заменяются на заглавные. Если заглавная буква превращается при транслитерации в несколько букв, то заглавной должна остаться только первая из них (например, «Ц» → «Tc»). Все некириллические символы должны остаться на месте.

Формат ввода
В одной папке с вашей программой лежит файл cyrillic.txt. В нём, в числе прочих, содержится некоторое количество кириллических символов.

Формат вывода
В файл transliteration.txt записать результат транслитерации исходного файла.

Пример 1
Ввод
    Привет, мир!
Вывод
    Privet, mir!

Пример 2
Ввод
    Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное виденье, Как гений чистой красоты.
Вывод
    Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, Kak mimoletnoe videne, Kak genii chistoi krasoty.

Ввод
cyrillic.txt

Вывод
transliteration.txt
"""