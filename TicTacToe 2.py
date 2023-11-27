def intro():
    print('''Welcome to Tic Tac Toe!
The rules are simple, the first one
to get 3 of their symbol in a row 
vertically, horizontally or diagonally wins!''')
def print_board():
    print('''This is the board -''')
    print('-', '|', '-', '|', '-')
    print('-', '|', '-', '|', '-')
    print('-', '|', '-', '|', '-')

def choose_xo():
    global pl
    pl = input('''Choose your symbol, X or O
''')
    if pl == "X":
        print("You have chosen X")
        pass
    elif pl == "O":
        print("You have chosen O")
        pass
    else:
        print("Invalid Input")
        exit()

def input_loc():
    global pl_row
    pl_row = int(input('''Please enter the row:
1 - Upper Row
2 - Middle Row
3 - Lower Row
'''))
    global pl_col
    pl_col = int(input('''Please enter the column:
1 - Left Column
2 - Middle Column
3 - Right Column
'''))

def check_input_rc():
    if pl_row == 1 or pl_row == 2 or pl_row == 3:
        pass
    elif pl_col == 1 or pl_col == 2 or pl_col == 3:
        pass
    else:
        print("Invalid Input")
        exit()

def place_sym_pl():
    p_1 = "-"
    p_2 = "-"
    p_3 = "-"
    p_4 = "-"
    p_5 = "-"
    p_6 = "-"
    p_7 = "-"
    p_8 = "-"
    p_9 = "-"
    if pl == "X":
        if pl_row == 1 and pl_col == 1:
            p_1 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 1 and pl_col == 2:
            p_2 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 1 and pl_col == 3:
            p_3 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 2 and pl_col == 1:
            p_4 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 2 and pl_col == 2:
            p_5 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 2 and pl_col == 3:
            p_6 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 3 and pl_col == 1:
            p_7 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 3 and pl_col == 2:
            p_8 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 3 and pl_col == 3:
            p_9 = "X"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        else:
            pass
    else:
        if pl_row == 1 and pl_col == 1:
            p_1 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 1 and pl_col == 2:
            p_2 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 1 and pl_col == 3:
            p_3 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 2 and pl_col == 1:
            p_4 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 2 and pl_col == 2:
            p_5 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 2 and pl_col == 3:
            p_6 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 3 and pl_col == 1:
            p_7 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 3 and pl_col == 2:
            p_8 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        elif pl_row == 3 and pl_col == 3:
            p_9 = "O"
            print('''This is the board -''')
            print(p_1, '|', p_2, '|', p_3)
            print(p_4, '|', p_5, '|', p_6)
            print(p_7, '|', p_8, '|', p_9)
        else:
            print("Invalid Input")
            exit()

def main():
    intro()
    print_board()
    choose_xo()
    input_loc()
    check_input_rc()
    place_sym_pl()
main()

