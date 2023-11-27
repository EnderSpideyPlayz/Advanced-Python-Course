from os import *
import random as r
print("To select a random element from a list")
e1 = [10,20,30,40,50]
print(r.choice(e1))
set = {1,2,3,4,5}
print(r.choice(list(set)))
dict = {
    "a" : "x",
    "b" : "y",
    "c" : "z"
}
d2 = r.choice(list(dict))
print(d2, dict[d2])
