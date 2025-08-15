course = '\nPython for Beginners'
print(course[0:7])

name = 'Jennifer'
print(name[1:-1])

print("\n")

name = 'Eliya C. Superio'
print(len(name)) #length of string
print(name.title()) #makes first letter of each word uppercase
print(name.upper()) #makes all letters uppercase
print(name.lower()) #makes all letters lowecase
print(name.find('C.')) #find the index of C.
print(name.replace('Superio', 'Eliya')) #replace superio with eliya
print('Eliya' in name) #bolean check if Eliya is in name True or False

print("\n")

# Arithmetic operators
print(1+2) # Addition
print(1-2) # Subtraction
print(1*2) # Multiplication
print(1/2) # Division
print(1%2) # Modulus
print(1**2) # Exponentiation
print(1//2) # Floor division

print("\n")

# Assignment operators
x = 10
x += 3 # x = x + 3
print(x)

print("\n")

# operators precedence PEMDAS
x = 10 - 3 + 2 # Addition and subtraction from left to right
xa = 10 + 3 * 2 # Multiplication before addition
xb = (2 + 3) * 10 - 3 # Parentheses first
print(x)
print(xa)
print(xb)

print("\n")
# Math Functions
import math

print(math.ceil(2.9)) # Rounds up to nearest integer
print(math.floor(2.9)) # Rounds down to nearest integer
x = 2.9
print(round(x)) # Rounds to nearest integer
print(abs(-2.9)) # Absolute value
# searh math module for more functions

print("\n")
#if statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day!")



print("\n")
#Logical Operators
#and, or, not
#and both conditions must be true
#or at least one condition must be true 
#not negates the condition
has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

elif has_high_income or has_good_credit:
    print("Eligible for loan")

elif not has_high_income:
    print("Not eligible for loan")









