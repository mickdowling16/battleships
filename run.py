import random

LENGTH_OF_SHIPS = [2,3,3,4,5]  
PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def welcome_message():
    print('Welcome to Battleships...\n')
    print("The aim of the game is to sink the computer's ships before they sink yours. Pick a row and column to make your guess...\n")
    player_name = input("Please enter your name here:\n")
    print("----------")

def print_board(board, user):
    print(f"{user} GAME BOARD")
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


welcome_message()
print_board(COMPUTER_BOARD, "COMPUTER")
print_board(PLAYER_BOARD, "YOUR")