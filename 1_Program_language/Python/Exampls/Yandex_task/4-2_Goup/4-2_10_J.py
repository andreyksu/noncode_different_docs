def secret_replace(textt, **replaces):
    listt = list(textt)
    for x in replaces:
        tuplee = replaces.get(x)
        countt = textt.count(x)
        while len(tuplee) < countt:
            tuplee += tuplee
        iterr = iter(tuplee)
        for pos in range(len(listt)):
            if listt[pos] == x:
                listt[pos] = next(iterr)
    return "".join(listt)


result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)

result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)

print(result)

"""
Ключевой секрет
Вася любит секреты и шифрование. Он часто пользуется шифром на основе замен и просит разработать вас функцию, которая позволит ему быстро шифровать сообщения.

Напишите функцию secret_replace(text, **replaces), которая принимает:

текст требующий шифрования;
именованные аргументы — правила замен, представляющие собой кортежи из одного или нескольких значений.
Функция должна вернуть зашифрованный текст.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Обратите внимание, что позиционный аргумент требуемой функции не должен иметь однобуквенного имени. Для понимания ошибки исследуйте следующих код:

def func(a, **b):
    ...

func(1, **{'a': 2})
Пример 1
Ввод
result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
Вывод
result = 'Hehiy123, wzrhid!'
Пример 2
Ввод
result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
Вывод
result = 'Z3X1-G!0Z371'
"""