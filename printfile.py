# File: printfile.py
# This program prints a file to the screen.

def main():
    filename = input("Enter the full file name: ")
    infile = open(filename, "r")
    data = infile.read()
    print(data)

main()