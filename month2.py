# File: month2.py
# This script is another program to print the month abbreviation when inputting its month number.

def main():
    # The variable "months" is a list used as a lookup table.
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = int(input("Enter the month number (1 - 12): "))

    # Print the result.
    print("\nThe month abbreviation is", months[n - 1] + ".")

main()