"""
High Level Programing Language
Simple Syntax
IDE Integrated Development Environment --> VSCode, PyCharm

"""

# print statement 
print("Hello World") # built in function that outputs text

# comments --> lines that are not executed by interpreter
"""
Multi Line Comment
1st
2nd
"""
# single line comment

# variables
    # names that store data in memory, created when value is assigned
    # no need of type declaration
    # start with a-z A-Z _
    # doesnt start with number
    # name, Name, NAME all are different variables
    # keywords cant be used as variables (ex: print, continue, break)
a = 45 # integer
b = 143.2 # float
c = "lol" # string

# Data Types
    # it defines what kind of data can a variable hold and operations it can perform
x = "Hello World" # string
x = 50  # integer
x = 60.5  # float
x = 3j  # complex
x = ["lol", "bob", "sos"]  # list 
x = ("lol", "bob", "sos")  # tuple
x = {"name": "loks", "age": 24} # dict
x = {"lol", "bob", "sos"} # set
x = True  # bool
x = b"lol" # binary  

# Input/Output
    # input() built in function that is used to take input from user
    # default data type is string
val = input() # No prompt
val = input("Enter Any Thing: ") # Prompt
print(val)
age = int(input("Enter Age : ")) # explict type conversion from string to int
print(type(age)) # type func to check type of variable

# Operators
    # Arithmetic operators
        # P E M D A S --> Parentheses Exponent Mul Div Add Sub
a = 9
b = 4
add = a + b  # 13 --> Addition
sub = a - b  # 5  --> Subtraction
mul = a * b  # 36 --> Multiplication
div = a / b  # 2.25 --> Division (Float)
fdiv = a // b  # 2 --> Floor Division (Rounds down value towards -infinite) 
mod = a % b  # 1 --> Remainder
exp = a ** b # 6561 --> exponent
try:
    print(10 / 0)
except:
    print("Error")
# Output: Error, %0 and //0 also gives error
print (10 //3) # 3
print(10 % 3) # 1
print(10 / 3) # 3.33333333333335
print(-10 //3) # -4
print(-10 % 3) # 2
print(10 // -3) # -4
print(10 % -3) # -2
print(5 // 2.0) # 2.0
print(5 % 2.0) # 1.0

    # Comparison operators
        # Used to compare two values, return boolean value
print(a == b)   # False, because 10 is not equal to 20
print(a != b)   # True, because 10 is not equal to 20
print(a > b)    # False, 10 is not greater than 20
print(a < b)    # True, 10 is less than 20
print(a >= b)   # False, 10 is not greater than or equal to 20
print(a <= b)   # True, 10 is less than or equal to 20

    # Logical operators
        # Logical AND, Logical OR, Logical NOT
a = True
b = False
print(a and b) # False --> Both true 
print(a or b)  # True --> Any one true 
print(not a) # False --> opposite 
# True == 1
# False == 0
print(~True) # -2 -> ~ (-2) explanation: true is 1, ~1 is -2
print(not True) # False

    # Bit wise operators
        # bit by bit operation
a = 10
b = 4
print(a & b) # 0
print(a | b) # 14
print(~a) # -11
print(a ^ b) # 14
print(a >> 2) # 2
print(a << 2) # 40

    # Assignment Operators
        # used to assign values
a = 10
b = a 
print(b) # 10
b += a 
print(b) # 20
b -= a 
print(b) # 10
b *= a 
print(b) # 100
b <<= a 
print(b) # 102400

# IF ELSE
    # if statements run when condition is true, else when false
# if else
i = 10
if (i > 0):
    print("greater")
else:
    print("lesser")
# if elif else
i = 10
if (i == 10):
    print(" i is 10")
elif (i == 100):
    print("i is 100")
else:
    print("i is something")

# Loops
    # For
        # iterate over sequence
for i in range(0, 10, 2): # start end step
    print(i)
    # While
        # continues as long as condition is true
count = 0
while (count < 3): 
    count = count + 1
    print("Hello")

# Functions
    # reusable code that performs specific task
    # built in --> print(), len()
    # user defined --> created using def keyword
    # def funcname(parameters):
def evenOdd(x): # func declaration
    if x % 2 == 0: # statement/body
        print("even")
    else:
        print("odd")
evenOdd(2) # func calling
