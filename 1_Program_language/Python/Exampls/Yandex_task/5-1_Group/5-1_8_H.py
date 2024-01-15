class Cell:
    def __init__(self, aState):
        self.statuss = aState
        self.position = None

    def setPosition(self, aPosition):
        self.position = aPosition

    def getPosition(self):
        return self.position

    def status(self):
        return self.statuss

    def set_status(self, aState):
        self.statuss = aState


class Checkers:
    def __init__(self):
        self.dictt = dict()
        self.initField()

    def initField(self):
        for pos, charr in enumerate("ABCDEFGH"):            
            for numm in range(1, 9):
                color = "X"
                if numm <= 3:
                    if numm % 2 == 0:
                        if pos % 2 != 0:
                            color = "W"
                    else:
                        if pos % 2 == 0:
                            color = "W"
                elif numm >= 6:
                    if numm % 2 == 0:
                        if pos % 2 != 0:
                            color = "B"
                    else:
                        if pos % 2 == 0:
                            color = "B"

                tmpPos = f"{charr}{numm}"
                self.dictt[tmpPos] = Cell(color)

    def move(self, f, t):
        f_cell = self.dictt[f]
        t_cell = self.dictt[t]

        f_state = f_cell.status()
        t_state = t_cell.status()

        f_cell.set_status("X")
        t_cell.set_status(f_state)

    def get_cell(self, position):
        return self.dictt[position]


checkers = Checkers()
for row in "87654321":
    for col in "ABCDEFGH":
        print(checkers.get_cell(col + row).status(), end="")
    print()


checkers = Checkers()
checkers.move("C3", "D4")
checkers.move("H6", "G5")
for row in "87654321":
    for col in "ABCDEFGH":
        print(checkers.get_cell(col + row).status(), end="")
    print()


"""
Шашки
Шашки очень занимательная игра, которую достаточно легко моделировать.

Правила подразумевают наличие двух классов: игральная доска и шашка. Однако мы немного упростим себе задачу и вместо шашки будем манипулировать клетками, которые могут находиться в трех состояниях: пустая, белая шашка и чёрная шашка.

Разработайте два класса: Checkers и Cell.

Объекты класса Checkers при инициализации строят игральную доску со стандартным распределением клеток и должны обладать методами:

move(f, t) — перемещает шашку из позиции f в позицию t;
get_cell(p) — возвращает объект «клетка» в позиции p.
Объекты класса Cell при инициализации принимают одно из трех состояний: W — белая шашка, B — чёрная шашка, X — пустая клетка, а также обладают методом status() возвращающим заложенное в ней состояние.

Координаты клеток описываются строками вида PQ, где:

P — столбец игральной доски, одна из заглавных латинских букв: ABCDEFGH;
Q — строка игральной доски, одна из цифр: 12345678.
Будем считать, что пользователь всегда ходит правильно и контролировать возможность хода не требуется.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    checkers = Checkers()
    for row in '87654321':
        for col in 'ABCDEFGH':
            print(checkers.get_cell(col + row).status(), end='')
        print()
Вывод
    XBXBXBXB
    BXBXBXBX
    XBXBXBXB
    XXXXXXXX
    XXXXXXXX
    WXWXWXWX
    XWXWXWXW
    WXWXWXWX
Пример 2
Ввод
    checkers = Checkers()
    checkers.move('C3', 'D4')
    checkers.move('H6', 'G5')
    for row in '87654321':
        for col in 'ABCDEFGH':
            print(checkers.get_cell(col + row).status(), end='')
        print()
Вывод
    XBXBXBXB
    BXBXBXBX
    XBXBXBXX
    XXXXXXBX
    XXXWXXXX
    WXXXWXWX
    XWXWXWXW
    WXWXWXWX
"""