#!/usr/bin/python3


class Peg(): 
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.__symbol = symbol

    def draw(self):
        print(self.__symbol, end='')

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol):
        self.__symbol = symbol


class CodePeg(Peg):
    size = 10
    default = '_'
    def __init__(self, x, y):
        super().__init__(x, y, CodePeg.default)


class KeyPeg(Peg):
    size = 5
    default = 'X'
    def __init__(self, x, y):
        super().__init__(x, y, KeyPeg.default)

class Row():
    cnt_pegs = 4
    def __init__(self, position, pegs=None):
        if  not pegs:
            pegs = Row.cnt_pegs
        self.k_pegs = [KeyPeg(x, position) for x in range(pegs)]
        self.c_pegs = [CodePeg(x, position) for x in range(pegs, 2 * pegs)]

    def draw(self):
        for kp in self.k_pegs:
            kp.draw()
        print(' | ', end='')
        for cp in self.c_pegs:
            cp.draw()

    def place(self, xPos, PegColor):
        self.c_pegs[xPos].symbol = PegColor



class Board:
    finished = False
    atRow = 0
    colors = {
            'Yellow':'Y',
            'Cyan':'C',
            'Magenta': 'M',
            'Red': 'R',
            'Blue': 'B',
            'White': 'W'
            }
    __code = None

    def __init__(self, columns=4, rows=9):
        self.__columns = columns
        self.__rows = rows

        Row.cnt_pegs = columns
        self.__rows = [Row(idx, columns) for idx in range(rows)]
        self.__code = Row(0, columns)
        """The code to crack"""
        color = None
        for i in range(self.__columns):
            print(Board.colors)
            while True:
                color = input("Enter letter for peg #{} Color: ".format(i + 1))
                if color in Board.colors.values():
                    break
            self.__code.place(i, color)
        print("\n<<< The code to Crack >>>")
        self.__code.draw()
        print('\n\n\n')


    def draw(self):
        for row in self.__rows:
            row.draw()
            print()

    def nextMove(self):
        """Human player"""
        color = None
        for i in range(self.__columns):
            print(Board.colors)
            while True:
                color = input("Enter letter for peg #{} Color: ".format(i + 1))
                if color in Board.colors.values():
                    break
            self.__rows[Board.atRow].place(i, color)
        Board.atRow += 1
        """Computer"""









if __name__ == '__main__':
    board = Board()
    while(not board.finished):
        board.draw()
        board.nextMove()
