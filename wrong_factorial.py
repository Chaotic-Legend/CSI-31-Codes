# Here is the introduction.
# File: wrong_factorial.py
# An incorrect program to calculate the factorial of a whole number.

def main():
    print("Incorrect Factorial")
    print()
    n = int(input("Enter a whole number: "))
    fact = 1
    for i in range(n):
        fact = fact * i
    print()
    print("The factorial of", n, "is not", fact)

main()
