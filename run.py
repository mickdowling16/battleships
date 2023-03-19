from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    Main board class. sets board size, number of ships and board type
    """

    def __init__(self, size, number_ships, name, type):
        self.size = size
        self.number_ships = number_ships
        self.board = [["." for x in range(size)] for y in range(size)]
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        for x in self.board:
            print(" ".join(x))

    def guesses(self, x, y)
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Missed"