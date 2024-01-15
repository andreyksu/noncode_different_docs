list_of_printed_str = set()

def modern_print(target_str):
    if target_str not in list_of_printed_str:
        print(target_str)
        list_of_printed_str.add(target_str)


modern_print("Ало!")
modern_print("Ало!")
modern_print("Я тебя не слышу")
modern_print("Ало!")
modern_print("Ало!")
modern_print("Позвони когда сможешь")
modern_print("Позвони когда сможешь")
modern_print("Я тебя не слышу")


"""
Модернизация системы вывода
Разработайте функцию modern_print, которая принимает строку и выводит её, если она не была выведена ранее.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")
Вывод
Hello!
How do you do?
Пример 2
Ввод
modern_print("Ало!")
modern_print("Ало!")
modern_print("Я тебя не слышу")
modern_print("Ало!")
modern_print("Ало!")
modern_print("Позвони когда сможешь")
modern_print("Позвони когда сможешь")
modern_print("Я тебя не слышу")
Вывод
Ало!
Я тебя не слышу
Позвони когда сможешь
"""