# Here is the introduction.
# File: arithmetic_seq.py
# A program to compute the 15-th term of an arithmetic sequence.

def main():
    print("This program calculates the fifteenth term of an arithmetic sequence.")
    term = eval(input("Enter the starting term: "))
    difference = eval(input("Enter the common difference: "))
    for i in range(15):
        print(term)
        term = term + difference
    
    print("The fifteenth term of this arithmetic sequence is", term)

main()
