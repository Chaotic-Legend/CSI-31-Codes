# Isaac D. Hoyos
# Test 1: Question 3

def main():
    print("This program calculates the tenth term of an arithmetic sequence.")
    term = float(input("Enter the starting term: "))
    difference = float(input("Enter the common difference: "))
    for i in range(10 - 1):
        print(term)
        term = term + difference
    print("The tenth term of this arithmetic sequence is", term)

main()