# File: average_of_two_numbers.py
# This script will find the average of two numbers.

def auxiliary(x,y):
    return (x + y) / 2

def main():
    print("This program prints the average of two numbers.")
    s1, s2 = eval(input("Enter two scores with a comma in between them: "))
    print("The average of your scores is", auxiliary(s1,s2))

main() 

print()

def main():
    print("This program prints the average of two numbers.")
    s1, s2 = eval(input("Enter two scores with a comma in between them: "))
    average = (s1 + s2) / 2
    print("The average of your scores is", average)

main()
