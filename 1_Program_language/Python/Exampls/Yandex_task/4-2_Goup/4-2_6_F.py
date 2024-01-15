menu = {
    "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
    "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
    "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
    "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1},
}

default_message = "К сожалению, не можем предложить Вам напиток"


def order(*argss):
    global in_stock
    for coffee_name in argss:
        menu_item = menu.get(coffee_name)
        for key in menu_item:
            ress = in_stock[key] - menu_item[key]
            if ress >= 0:
                continue
            else:
                break
        else:
            for i in in_stock:
                in_stock[i] = in_stock[i] - menu_item[i]
            return coffee_name
    else:
        return default_message


in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))


in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(
    order(
        "Эспрессо",
        "Капучино",
        "Макиато",
        "Кофе по-венски",
        "Латте Макиато",
        "Кон Панна",
    )
)
print(
    order(
        "Эспрессо",
        "Капучино",
        "Макиато",
        "Кофе по-венски",
        "Латте Макиато",
        "Кон Панна",
    )
)


"""
Кофейня
Руководство местной кофейни для программистов под названием Java-0x00 решило модернизировать систему заказа кофе.

Для этого им требуется реализовать функцию order, которая принимает список предпочтений посетителя в порядке «убывания желания».

Согласно положению, каждый напиток в кофейне строго определён рецептом:

Эспрессо готовится из: 1 порции кофейных зерен.
Капучино готовится из: 1 порции кофейных зерен и 3 порций молока.
Макиато готовится из: 2 порций кофейных зерен и 1 порции молока.
Кофе по-венски готовится из: 1 порции кофейных зерен и 2 порций взбитых сливок.
Латте Макиато готовится из: 1 порции кофейных зерен, 2 порций молока и 1 порции взбитых сливок.
Кон Панна готовится из: 1 порции кофейных зерен и 1 порции взбитых сливок.
В глобальной переменной in_stock содержится словарь, описывающий ингредиенты в наличии. Ключи словаря: coffee, cream, milk.

Функция должна вернуть:

название напитка, который будет приготовлен;
сообщение «К сожалению, не можем предложить Вам напиток», если ни одно из предпочтений не может быть приготовлено.
Если заказ, может быть совершён, количество доступных ингредиентов должно соответствующим образом уменьшиться.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
Вывод
Эспрессо
К сожалению, не можем предложить Вам напиток
Пример 2
Ввод
in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
Вывод
Капучино
Макиато
Эспрессо
"""