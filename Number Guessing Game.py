import random as r
u = int(input("Enter a number between 1 and 100 "))
c = r.randint(1,101)
print("The computer has chosen", c)
if u > c:
    print("You have won! You chose ", u, "which is greater than", c)
elif u == c:
    print("The numbers are equal. Its a tie!")
else:
    print("The computer wins! Better luck next time! You chose ", u, "which is lesser than ", c)