#!/usr/bin/python3
from copy import deepcopy

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
    default = '.'
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
        print('\t\t', end='')
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
        self.__cnt_columns = columns
        self.__cnt_rows = rows

        Row.cnt_pegs = columns
        self.__rows = [Row(idx, columns) for idx in range(rows)]
        self.__code = Row(0, columns)
        """The code to crack"""
        color = None
        for i in range(self.__cnt_columns):
            print(Board.colors)
            while True:
                color = input("Enter letter for peg #{} Color: ".format(i + 1))
                color = color.upper()
                if color in Board.colors.values():
                    break
            self.__code.place(i, color)
        print("\n\t<<< The code to Crack >>>")
        self.__code.draw()
        print('\n\n\n')


    def draw(self):
        print('\n\t\tMastermind!')
        for row in self.__rows:
            row.draw()
            print()
        print()

    def nextMove(self):
        """Gets the player's Input and then process the Computer response."""
        # Human player
        color = None
        row = self.__rows[Board.atRow]
        for i in range(self.__cnt_columns):
            print(Board.colors)
            while True:
                color = input("Enter letter for peg #{} Color: ".format(i + 1))
                color = color.upper()
                if color in Board.colors.values():
                    break
            row.place(i, color)
        # Computers Turn
        cp_row = row.c_pegs
        k_pegs = row.k_pegs
        cnt_kpeg = 0
        CODE = deepcopy(self.__code.c_pegs)
        # First check those that are the right color at right position
        for i in range(self.__cnt_columns):
            if CODE[i].symbol == cp_row[i].symbol:
                k_pegs[cnt_kpeg].symbol = 'b'
                cnt_kpeg += 1
                CODE[i].symbol = None
        if cnt_kpeg == self.__cnt_columns:
            Board.finished = True
            print("\n\t\tGAME WON!  Congratulations!!\n")
            print("\tCode to Crack ", end='')
            self.__code.draw()
            print()
            return
        # Now checks for the correct colors but out of position
        for i in range(self.__cnt_columns):
            for j in range(self.__cnt_columns):
                if CODE[i].symbol == cp_row[j].symbol:
                    k_pegs[cnt_kpeg].symbol = 'w'
                    cnt_kpeg += 1
                    CODE[j].symbol = None
        # Moves the board up to the next row, and check if the end of the game
        Board.atRow += 1
        if Board.atRow == self.__cnt_rows:
            Board.finished = True
            print("\n\t\tGame Over!  YOU LOST!!\n")
            print("\tThe code was: ", end='')
            self.__code.draw()
            print('\n')


if __name__ == '__main__':
    board = Board()
    while(not board.finished):
        board.draw()
        board.nextMove()
