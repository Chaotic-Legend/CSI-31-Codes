# File: average_of_two_numbers.py
# A program to find the average of two numbers.

def main ():
    print("This program prints the average of two numbers.")
    s1 , s2 = eval(input("Enter two scores with a comma in between them: "))
    average = (s1 + s2) / 2
    print("The average of your scores is" , average)

main ()