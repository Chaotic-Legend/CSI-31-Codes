# Here is the introduction.
# File: geometric_seq.py
# This program computes the nth term of a geometric sequence.

def main():
    print("This program calculates the nth term of a geometric sequence.\n")
    term = float(input("Enter the starting term: "))
    ratio = float(input("Enter the common ratio: "))
    nth = eval(input("Enter the nth term: "))
    for i in range(nth - 1):
        print(term)
        term = term * ratio
    print("The", nth, "term of this geometric sequence is", term)

main()
