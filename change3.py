# Here is the introduction.
# File: change3.py
# A third program to count your loose change to show the total amount in dollars.

def main():
    print("This program is a loose change counter that gives the total value in dollars.\n")
    print("Please enter the exact number of coins you have for each type of coin.")
    dollarcoin = int(input("Dollar Coins: "))
    halfdollar = int(input("Half Dollar Coins: "))
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total = dollarcoin * 100 + halfdollar * 50 + quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1
    print("\nThe total value of your loose change in dollars is ${0}.{1:0>2}.".format(total // 100, total % 100))

main()