text = "Мама мыла раму!"

text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''

print((list(text)))

strr = {y: text.lower().count(y) for y in [x for x in sorted(list(text.lower())) if x.isalnum()]}
print(strr)


"""
Буквенная статистика
Вашему решению будет предоставлена строка text.

Напишите выражение для генерации словаря, который содержит информацию о частоте употребления букв в заданной строке.

При анализе не учитывайте регистр, а ключами словаря сделайте использованные в строке буквы в нижнем регистре.

Примечание
В решении не должно быть ничего, кроме выражения.

Пример 1
Ввод
text = 'Мама мыла раму!'
Вывод
{'а': 4, 'л': 1, 'м': 4, 'р': 1, 'у': 1, 'ы': 1}
Пример 2
Ввод
text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''
Вывод
{   'а': 6,
    'в': 2,
    'д': 5,
    'е': 7,
    'з': 2,
    'и': 5,
    'к': 1,
    'л': 2,
    'м': 3,
    'н': 3,
    'о': 3,
    'п': 2,
    'р': 1,
    'с': 1,
    'т': 1,
    'х': 1,
    'ё': 1}
"""