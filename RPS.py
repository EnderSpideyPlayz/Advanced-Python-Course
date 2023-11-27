import random as r
def rps():
    ucount = 0
    ccount = 0
    l = ["ROCK", "PAPER", "SCISSORS"]
    while True:
        a = input('''
Game start...
1 Yes
2 No/Exit ''')
        if a == "1":
         for a in range(1,6):
            u = int(input('''
1 ROCK
2 SCISSORS
3 PAPER
    '''))
            if u == 1:
                j = "ROCK"
            elif u == 2:
                j = "SCISSORS"
            elif u == 3:
                j = "PAPER"
            else:
                print("Invalid Input")
            ch = r.choice(l)
            print("The computer has chosen, ", ch)
            if ch == j:
                print("Its a draw.")
                print("You chose ", j)
                print("The computer chose, ", ch)
            elif j == "ROCK" and ch == "SCISSORS" or j == "SCISSORS" and ch == "PAPER" or j == "PAPER" and ch == "ROCK":
                print("User wins the game")
                print("User chose ", j)
                ucount = ucount+1
            else:
                print("Computer wins the game")
                print("Computer chose ", ch)
                ccount = ccount + 1
            if ucount > ccount:
                print("USER WINS, ", ucount, ":", ccount)
            elif ccount > ucount:
                print("COMPUTER WINS", ucount, ":", ccount)
            else:
                print("ITS A DRAW")
        else:
            break

rps()