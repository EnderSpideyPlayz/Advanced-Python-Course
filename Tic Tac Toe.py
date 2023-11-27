import random as r
def main():
    intro()
    board = create_grid()
    print(board)
    decide_sym()
    start_game(board, symbol_1, symbol_2 , count)
def intro():
    print("Welcome to my Python Tic Tac Toe Game")
    print("The rules are as follows:")
    print("Each player takes turns and is given either X or O")
    print("This takes place in a 3 by 3 grid")
    print("The first to get three symbols of their own in")
    print("a straight line either vertically or horizontally wins")
def create_grid():
    print("This is the board")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board
def decide_sym():
    symbol_1 = input("Player 1, do you want to be X or O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are 0")
        return symbol_1
        return symbol_2
    elif symbol_1 == "O":
        symbol_2 = "X"
        print("Player 2, you are X")
        return symbol_1
        return symbol_2
    else:
        print("Invalid Input")

def start_game(board, s1, s2, count):
    if r.randint(1,2) == "1":
        c_player = s1
        print("Player" , c_player, "it is your turn")
    else:
        c_player = s2
        print("Player", c_player, "it is your turn")
    c_row = int(input('''Pick a row:
    [1 : Upper Row, 2 : Middle Row, 3 : Lower Row]'''))
    c_column = int(input('''Pick a row:
    [1 : Left Column, 2 : Middle Column, 3 : Upper Column]'''))
    def range_c
main()