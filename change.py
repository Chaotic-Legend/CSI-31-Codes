# Here is the introduction.
# File: change.py
# This script counts loose change to give the total value in dollars.

def main():
    print("This program is a loose change counter that gives the total value in dollars.")
    print()
    print("Please enter the exact number of coins you have for each type of coin.")
    dollarcoin = eval(input("Dollar Coins: "))
    halfdollar = eval(input("Half Dollar Coins: "))
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickles: "))
    pennies = eval(input("Pennies: "))
    total = dollarcoin * 1.00 + halfdollar * 0.50 + quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    print()
    print("The total value of your loose change in dollars is", round(total, 3))

main()
