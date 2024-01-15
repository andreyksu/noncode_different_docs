inputed_str = input()

dict_of_morze = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

upper_str = inputed_str.upper()
splited_str = upper_str.split()

# print(f"upper_str = {upper_str}, splited_str = {splited_str}")

for i in splited_str:
    for j in i:
        print(dict_of_morze[j], end=" ")
    print()


"""
Азбука Морзе
Вам дан английский текст. Закодируйте его с помощью азбуки Морзе Каждая буква заменяется на последовательность точек и тире. В качестве тире используйте обычный дефис: -, а в качестве точки — точку .. Например, буква g превратится в трёхсимвольную строку --.. Между закодированными буквами ставится ровно один пробел. Например, слово Help превратится в .... . .-.. .--.. Обратите внимание, что строчные и заглавные буквы кодируются одинаково.

Формат ввода
Весь текст записан в единственной строке. Текст состоит из английских букв и пробелов, других символов в тексте нет. В тексте не может быть двух или более пробелов подряд.

Формат вывода
Выведите каждое слово исходного текста, закодированное азбукой Морзе, на отдельной строке.
Количество строк в ответе должно совпадать с количеством слов в исходном тексте.

Примечание
Один из вариантов словаря с Азбукой Морзе:

    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
Пример 1
Ввод
Hello world
Вывод
.... . .-.. .-.. ---
.-- --- .-. .-.. -..
Пример 2
Ввод
Help me SOS
Вывод
.... . .-.. .--.
-- .
... --- ...
"""