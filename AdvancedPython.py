import random as r
import os
#Methods --> Perform Tasks
#User Defined or Predefined
#User Defined Function = Method

#Interpreter --> Line by line, stops at wrong line, running program, translates code into human lang. and vice versa
#Compiler -->

#User Def Keyword:
#Sum is func. name

# def sum(a,b):
#     c = a + b
#     print(c)
#
# sum(1,2)

#Examples:

# def Heading():
#     print("Welcome to Python")
# Heading()

def Multiply(a,b):
    print(a*b)
# Multiply(1,2)

#Module --> File containing methods, classes or vars, etc.
#User Defined Modules
#Predefined Modules
def sum3(a,b,c):
    d = a + b + c
    print(d)
def sum2(a,b):
    c = a + b
    print(c)
# #import j
# print(j.sum(10,20))

def factorial(f):
    j = 0
    a = 1
    if f ==0:
        print("1")
    else:
        for i in range(1,f):
            a = a*i
        print(f*a)

#LAMBDA FUNCTION OR ITERATOR
double = lambda x:x*2
# print(double(2))

average = lambda x,y,z:(x+y+z)/3
# print(average(2,3,4))

def add5(x,y):
    return 5+x(y)
cube = lambda x:x**3
# print(add5(cube,2))


#OOPS Object Oriented Programming Language
#OOPS --> Security

# class student:
#     s_rollno = 10
#     s_name = "abc"
#     s_marks = 96
#     def student_behaviour(self):
#         print("Student's behaviour is very good!")
# o=student()
# print(o.s_name,o.s_rollno,o.s_marks)
# o.student_behaviour()

# class A:
#     a = 10
#     b = 20
#     print(a, b)
#     def demo(self):
#         print("Hello to class A!")
#     def add(self):
#         c = self.a+self.b
#         print(c)
# o=A()
# o.demo()
# o.add()

#Random No. Program
# print(r.randrange(1,10,3))
# print(r.randrange(1,10,3))
#Randrange goes (1,n-1)
#Randint goes (x,y)
#Increment in randrange steps up 3, randrange(1,10,3) = 1,4,7

# l = [1,2,3,4,5]
# x = r.shuffle(l)
# print("The shuffled list is: ",l)

#OS MODULE

# print(r.choice(os.listdir("/")))
#WILL PRINT RANDOM FILE FROM C DRIVE

# import random as r
# l = ["a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# a = r.choice(l)
# x = int(input("How many letters should be there in each word? "))
# for i in range(1,x):
#     a = a + r.choice(l)
# print(a)

#Expression In Python --> PEDMAS --> Parenthesis Exponent Division Multiplication Addition Subtraction

# a = 12 - 3 + 4*(1/2)
# print(a)

# print(34+12-4*5/6*2)

#C --> No Security
#C++ --> OOPS Started, Security
#Java --> Very Secure, Pure OOPS
# OOPS - Object Oriented Program
# Class - Defines properties and behaviours of object
# Object - Access class properties and methods
# class student:
#     student_name = "abc"
#     student_rollno = 12
#     student_marks = 24
#     def studentbehaviour(self):
#         print("The student's behaviour is good")
#         print("The student is good in maths")

# o = student()
# o.studentbehaviour()
# print(o.student_marks)
# print(o.student_name)
# print(o.student_rollno)

# Single Inheritance
# Class A is Super Class and others are subclass
# class a:
#     def demo(self):
#         print("Hello to class A")
# class b(a):
#     def demo1(self):
#         print("Hello to class B")
# o=b()
# o.demo()
# o.demo1()

def table():
    x = int(input("Enter your number "))
    j = int(input("Please enter the upper limit to which the table should run to "))
    for i in range(1,j+1):
        print(i*x)

# class student:
#     a = r.randint(1,100)
#     b = r.randint(1,100)
#     def intro(self):
#         print("Welcome! This will generate two random numbers between 1 and 100 and add them")
#     def sum(self):
#         a = self.a
#         b = self.b
#         print("The numbers are : ", a, ",", b, ". Their sum is : ", a + b)
# o = student()
# o.intro()
# o.sum()

#INHERITANCE--> 1 Object to access multiple classes

#Single Inheritance --> One Superclass One Subclass

#B(A) --> B is subclass and A is superclass

class inh_test_A:
    def demo1(self):
        print("Welcome to Class A")
class inh_test_B(inh_test_A):
    def demo2(self):
        print("Welcome to Class B")
# obj = inh_test_B()
# obj.demo2()
# obj.demo1()

#Multi Levelled Inheritance

class inh_test_C(inh_test_B):
    def demo3(self):
        print("Welcome to Class C")
class inh_test_D(inh_test_C):
    def demo4(self):
        print("Welcome to Class D")

# obj=inh_test_D()
# obj.demo1()
# obj.demo2()
# obj.demo3()
# obj.demo4()

#Multiple Inheritance
class inh_test_A:
    def demo1(self):
        print("Welcome to Class A")
class inh_test_B():
    def demo2(self):
        print("Welcome to Class B")
class inh_test_C():
    def demo3(self):
        print("Welcome to Class C")
class inh_test_D(inh_test_A,inh_test_B,inh_test_C):
    def demo4(self):
        print("Welcome to Class D")

# obj = inh_test_D()
# obj.demo1()
# obj.demo2()
# obj.demo3()
# obj.demo4()

# class constructor_test:
#     def __init__(self):
#         print("Default Message")
# XYS = constructor_test()

#Encapsulation

# class abc:
#     def __init__(self):
#         __a = 10
#         print(__a)
#         self.__demo()
#     def __demo(self):
#         print("hello to python")
# o = abc()

#o = A() is a default constructor

#Polymorphism --> Multiple methods
#Method Overloading --> Same func. name but different parameters
#Method Overriding -->
# l=[10,20,30,40,50]
# print(len(l))
# l="Happy"
# print(len(l))

#REVISION

#CONSTRUCTOR
#Auto-call methods or variables
# class Ag:
#     a=10
#     def show(self):
#         print("Hello to Class Ag")
#     def __init__(self):
#         print("Hello to Class",self.a)
# obj=Ag()

# class Ag:
#     __a = 10
#     def __init__(self):
#         print("Hello, your marks are",self.__a)

#POLYMORPHISM = METHOD OVERLOADING
#The same function is used multiple times with different parameters
# l = [10,20,30,40,50]
# print(len(l))
# l = "excited"
# print(len(l))

class Ag:
    def show(self,name=""):
        print("Welcome to class 10,", name)
# obj=Ag()
# obj.show()
# obj.show("Darsh")

class A:
    def area(self,x="",y=0):
        if x!=0 and y!=0:
            print(x*y)
        elif x!=0:
            print(x**2)
        else:
            print("There is no area")
# obj = A()
# obj.area(10,20)
# obj.area(10)

#METHOD OVERRIDING

#METHOD NAME AND MULTIPLE METHODS USING SINGLE INHERITANCE
#SUPER KEYWORD TO CALL THE METHOD FROM SUPER CLASS
#OTHERWISE THE MOST RECENT ONE WILL WORK
# class A:
#     def show(self):
#         print("Welcome to Class A")
# class B(A):
#     def show(self):
#         super().show()
#         print("Welcome to Class B")
# obj = B()
# obj.show()

#GETTER SETTER METHOD
class A:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self, name):
        self.__name = name
# obj = A()
# obj.setname("Hi")
# print(obj.getname())

