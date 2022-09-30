# Here is the introduction.
# File: arithmetic_seq.py
# This script computes the nth term of an arithmetic sequence.

def main():
    print("This program calculates the nth term of an arithmetic sequence.")
    term = float(input("Enter the starting term: "))
    difference = float(input("Enter the common difference: "))
    nth = eval(input("Enter the nth term: "))
    for i in range(nth):
        print(term)
        term = term + difference
    print("The", nth, "term of this arithmetic sequence is", term)

main()
