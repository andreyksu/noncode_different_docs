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
