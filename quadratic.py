# Here is the introduction.
# File: quadratic.py
# A program that computes the real roots of a quadratic equation and illustrates the use of the math library.
# Note: The program crashes if there is no real root for the equation.

import math # This module makes the math library available to use.

def main():
    print("This program finds the real roots to a quadratic equation.")
    print()

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    
    print()
    
    print("The two roots are" , root1 , root2)

main()