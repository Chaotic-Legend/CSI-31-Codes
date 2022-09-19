# Here is the introduction.
# File: factorial.py
# A program to calculate the factorial of a whole number.
    
def main():
    print("Correct Factorial")
    print()
    n = int(input("Enter a whole number: "))
    
    fact = 1
    for i in range(1 , n + 1):
        fact = fact * i
    
    print()
    print("The factorial of " , n , " is " , fact)

main()