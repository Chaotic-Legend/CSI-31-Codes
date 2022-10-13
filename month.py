# File: month.py
# This program prints the abbreviation of a month when inputting its month number.

def main():
    # The variable "months" is a list used as a lookup table.
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter the month number (1 - 12): "))

    # Compute the starting position of the month with the variable n.
    pos = (n - 1) * 3

    # Grab the correct abbreviation from the "months" variable.
    monthAbbreviation = months[pos:pos + 3]

    # Print the result.
    print("\nThe month abbreviation is", monthAbbreviation + ".")

main()