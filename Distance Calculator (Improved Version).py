'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import math

# Ask the user to enter the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Ask the user to enter the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result rounded to two decimal places
print(f"The distance between the two points is: {distance:.2f}")