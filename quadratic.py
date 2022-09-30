# Here is the introduction.
# File: quadratic.py
# This script computes the real roots of a quadratic equation, evaluates the quadratic equation, and also illustrates the use of the math library.
# Note: This program will tell if there is no real root for the quadratic equation.

import math # This module makes the math library available to use.

def main():
    print("This script finds the real roots of a quadratic equation and evaluates the quadratic equation.")
    print()
    a = float(input("Enter the coefficient for a: "))
    b = float(input("Enter the coefficient for b: "))
    c = float(input("Enter the coefficient for c: "))
    x = float(input("Enter the value for x to evaluate: "))
    value = (a * (x**2) + b * x + c)
    disc = (b**2 - 4 * a * c)
    if disc < 0:
        print()
        print("Sorry, your quadratic equation has no real roots.")
    else:
        discRoot = math.sqrt(disc)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print()
        print("The two roots of this quadratic equation are", root1, "and", root2)
        print("The evaluation at x =", x, "is", value)

main()
