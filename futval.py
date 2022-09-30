# Here is the introduction.
# File: futval.py
# A program to compute the value of an investment carried out in a specific amount of years into the future.

def main():
    print("This program calculates the future value of an investment in a specific amount of years.")
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = eval(input("How many years should we look ahead? "))
    for i in range(years):
        principal = principal * (1 + apr)
    
    print("The value of your investment in", years, "years is", principal, "dollars.")

main()
