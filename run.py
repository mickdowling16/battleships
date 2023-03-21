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

    def guesses(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Missed"

    def add_ships(self, x, y, type="computer"):
        if len(self.ships) >= self.number_ships:
            print("Error: You cannot add more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def random_point(size):
    """
    Helper function to return random point
    """
    return randomint(0, size - 1)

def validate_coordinates(x, y, board):
    """
    Validates coordinates given and returns error if invalid value given
    """

def populate_board(board):
    """
    Populates game boards for computer
    """
 
def make_guess(board):
    """
    Allows users to input they're guesses
    """

def play_game(computer_board, player_board):
    """
    The main play game function
    """

def new_game():
    """
    Starts new game and sets board size and number of ships
    """
    size = 5
    number_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("Welcome to Battleships. The aim of the game is the sink all the enemy ships")
    print("Here is the game legend\n")
    print(f"Number of ships = {number_ships}")
    print("Direct Hit = *")
    print("Miss = X")
    print("Ships = @")
    print("The top left corner is row: 0 column: 0")
    print("----------\n")
    player_name = input("Please Enter Your Name: \n")

    computer_board = Board(size, number_ships, "Computer", type="computer")
    player_board = Board(size, number_ships, player_name, type="player")

    for _ in range(number_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)


new_game()