n = int(input("Enter Your No."))
f=1
if n < 0:
    print("Sorry there is no factorial for negative numbers")
elif n ==0:
    print("Factorial of zero is 1")
else:
    for i in range(1, n + 1):
        f = f * i
    print("Factorial of", n , "is", f)