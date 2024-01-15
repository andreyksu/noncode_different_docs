def can_eat(horse_point, other_point):
    horse_move_2y = [(-1, -2), (1, -2), (-1, 2), (1, 2)]
    horse_move_2x = [(-2, -1), (-2, 1), (2, -1), (2, 1)]
    whole_combination = horse_move_2y + horse_move_2x
    for point_to_move in whole_combination:
        x = point_to_move[0] + horse_point[0]
        y = point_to_move[1] + horse_point[1]
        if int(x) == int(other_point[0]) and int(y) == int(other_point[1]):
            return True
    else:
        return False


print(can_eat((2, 1), (4, 2)))
print(can_eat((5, 5), (6, 6)))


"""
Шахматный «обед»
Напишите функцию can_eat, которая принимает положение коня и другой фигуры в виде кортежей из двух координат, а возвращает булево значение: True если конь съедает фигуру и False иначе.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
result = can_eat((2, 1), (4, 2))
Вывод
result = True
Пример 2
Ввод
result = can_eat((5, 5), (6, 6))
Вывод
result = False
"""