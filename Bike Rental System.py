class bikeshop:
    def __init__(self, stock1):
        self.stock1 = stock1
    def display(self):
        print("Total bikes available are, ", self.stock1)
    def rentbike(self, q):
        if q<=0:
            print("Only a positive number of bikes can be rented")
        elif q>self.stock1:
            print("Only ", self.stock1, " bikes are available.")
        else:
            self.stock1 = self.stock1 - q
            print("Total price per hour is, Rupees ", q * 100)
            print(self.stock1, " bikes are remaining")

obj = bikeshop(50)
for a in range(1,11):
    if obj.stock1 <= 0:
        print("We are out of bikes. Pls come back later ")
    else:
        pass
    u = int(input('''
1 Display Stock
2 Rent a Bike
3 Exit 
'''))
    if u == 1:
        obj.display()
    elif u == 2:
        n = int(input("How many bikes do you want to rent? "))
        obj.rentbike(n)
    else:
        print("Thank you for checking out our store. Pls visit again!")
        exit()