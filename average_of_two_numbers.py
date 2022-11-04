# File: average_of_two_numbers.py
# This program will find the average of two numbers.

def auxiliary(x,y):
    return (x + y) / 2

def main():
    print("This program calculates the average of two numbers.\n")
    s1, s2 = eval(input("Enter two scores with a comma in between them: "))
    print("\nThe average of your two scores is {0}".format(auxiliary(s1, s2)))

main() 

print()

def average():
    print("This second program calculates the average of two numbers.\n")
    s1, s2 = eval(input("Enter two scores with a comma in between them: "))
    average = (s1 + s2) / 2
    print("\nThe average of your two scores is {0}".format(average))

average()
