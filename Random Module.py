import random as r
# print(r.randint(5,10))

# print(r.randrange(1,2))

#TO PRINT FLOATS BETWEEN 1 AND 0
# print(r.random())

# print(r.uniform(5,10))
#
# l = [1,2,3,4,5,6]
# print(r.choice(l))

# l = ["red", "blue", "green", "yellow"]
# print(r.choice(l))

# r.shuffle(l)
# print(l)

s1 = "X"
s2 = "O"
if r.randint(1, 2) == 1:
    c_player = s1
    print("Player", c_player, "it is your turn")
else:
    c_player = s2
    print("Player", c_player, "it is your turn")
c_row = int(input('''Pick a row:
[1 : Upper Row, 2 : Middle Row, 3 : Lower Row] '''))
c_column = int(input('''Pick a column:
[1 : Left Column, 2 : Middle Column, 3 : Upper Column] '''))