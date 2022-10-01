# Here is the introduction.
# File: change2.py
# A different script to count your loose change to calculate the total value in dollars.

def main():
    print("This program is a loose change counter that gives the total value in dollars.")
    print()
    print("Please enter the exact number of coins you have for each type of coin.")
    dollarcoin = int(input("Dollar Coins: "))
    halfdollar = int(input("Half Dollar Coins: "))
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total = dollarcoin * 1.00 + halfdollar * 0.50 + quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    print()
    print("The total value of your loose change in dollars is", total)

main()
