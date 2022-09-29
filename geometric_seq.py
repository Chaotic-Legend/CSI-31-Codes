# Here is the introduction.
# File: geometric_seq.py
# A program to compute the 15-th term of geometric sequence.

def main():
    print("This program calculates the fifteenth term of a geometric sequence.")
    term = eval(input("Enter the starting term: "))
    ratio = eval(input("Enter the common ratio: "))
    for i in range(15):
        print(term)
        term = term * ratio

    print("The fifteenth term of this geometric sequence is", term)

main()
