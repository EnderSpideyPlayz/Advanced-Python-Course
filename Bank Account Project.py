class bank_account:
    def __init__(self):
        self.amount=0
    def deposit(self, amount2, p):
        self.amount= self.amount+amount2
        print("The amount of ",amount2," has been deposited ")
    def withdraw(self, amount3, p):
        if amount3 > 0:
            pass
        else:
            print("Invalid Amount")
            pass
        if(self.amount-amount3>=500):
            self.amount=self.amount-amount3
            print("The amount of ",amount3," has been withdrawn ")
        else:
            print("Insufficient bank balance")
            print("There must be at least 500 Rs in the bank account at all times. ")
    def show_bal(self, amount, p):
        print("You current bank balance is, ", amount)
a=bank_account()

p = str(input("Enter your password "))
if p!= "Darsh_123":
    print("Incorrect Password")
    exit()
else:
    pass
while 1 > 0:
    p = int(input('''
1. Withdraw
2. Deposit
3. Check Balance
4. Exit '''))
    if p == 1:
        x = int(input("Enter the amount you want to withdraw "))
        a.withdraw(x, p)
    elif p == 2:
        y = int(input("Enter the amount you want to deposit "))
        a.deposit(y, p)
    elif p == 3:
        a.show_bal(a.amount, p)
    elif p == 4:
        print("Thank you for choosing us. Please come back again! Have a great day! ")
        exit()
    else:
        print("Invalid Input ")






















