# first python code
print("Hii kritika code are running or not")
print("Welcome to Python programming")

#Data types in python
name="Kritika"
age=22
height=5.6
is_student=True
print("Name:",name)
print("Age:",age)
print("Height:",height)
print("Is Student:",is_student)
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Variables and basic operations
a=10 
name="Kritika"
PI=3.14
print("Value of a:",a )
print("Name:",name)
print("Value of PI:",PI)
print("Sum of a and 5:",a+5)

# Keywords in python
import keyword
print("Python Keywords:",keyword.kwlist)
print("Total number of keywords:",len(keyword.kwlist))

# Comments in python
# This is a single line comment
"""
This is a
multi-line comment
"""
print("Comments in python are ignored by the interpreter")

#Style guide
total_price=100
tax_rate=0.05
final_price=total_price + (total_price * tax_rate)
print("Final Price:",final_price)

# To calculate sum of two numbers
num1=15
num2=25
sum=num1 + num2
print("Sum of",num1,"and",num2,"is:",sum)

#Operators in python
x=20
y=5
print("Addition:",x + y)  #addition
print("Subtraction:",x - y)  #subtraction
print("Multiplication:",x * y)  #multiplication
print("Division:",x / y)  #float division
print("Floor Division:",x // y)  #integer division
print("Modulus:",x % y)  #remainder
print("Exponentiation:",x ** y)  #power calculation

# Comparison / Relational operators
a=10
b=20
print("a == b:",a == b)  #equal to
print("a != b:",a != b)  #not equal to
print("a > b:",a > b)    #greater than
print("a < b:",a < b)    #less than
print("a >= b:",a >= b)  #greater than or equal to
print("a <= b:",a <= b)  #less than or equal to

# Assignment operators
m=5
n=10
m += 3  # m = m + 3
m -= 2  # m = m - 2
n /= 2  # n = n / 2
n *= 2  # n = n * 2
print("Value of m after += 3:",m)
print("Value of m after -= 2:",m)
print("Value of n after /= 2:",n)
print("Value of n after *= 2:",n)

# Logical operators
p=True
q=False
print("p and q:",p and q)  #logical AND
print("p or q:",p or q)    #logical OR
print("not p:",not p)      #logical NOT

#practies problemsX
X=3
X+=5
print(X)
X*=2
print("Value of X after *=2:",X)
X-=4
print(X)
X//=3
print(X)
X**=2
print(X)

#Operators precedence
result=10 + 5 * 2 ** 2 - (8 / 4)  #BODMAS
print("Result of the expression is:",result)
#same precedence operators evaluated left to right
value=20 - 5 + 3 # 10/2*5
print("Value of the expression is:",value)

#Type conversion in python
# two types of type conversion 1.Implicit 2.Explicit 
num_int=10 # allow to convert integer to float
num_float=float(num_int)
print("Integer value:",num_int)
print("Converted to float:",num_float)
num_float2=15.75 # allow to convert float to integer
num_int2=int(num_float2)
print("Float value:",num_float2)
print("Converted to integer:",num_int2)

a=3
b=5
print(type(a/b))

ans1=int(5+10.0)  #casting float to int
ans2=5+10.0 #conversion
print("ans1:",ans1,"Type:",type(ans1))
print("ans2:",ans2,"Type:",type(ans2))

#User input in python
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hello",name+"! You are",age,"years old.")

# sum s of two numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1 + num2
print("Sum of",num1,"and",num2,"is:",sum)

# print average of two numbers
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number:"))

average=(num1+num2)/2
print("Average of",num1,"and",num2,"is:",average)



