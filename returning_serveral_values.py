# File: returning_serveral_values.py
# This program returns several values to the user.

def operations():
    m, n = input("Enter two numbers to calculate: ").split(",")
    n = float(n)
    m = float(m)
    addition = m + n
    subtraction = m - n
    multiplication = m * n
    division = m / n

    return addition, subtraction, multiplication, division

print("\nThe sum, difference, product, and quotient of these two numbers are {0}.".format(operations()))