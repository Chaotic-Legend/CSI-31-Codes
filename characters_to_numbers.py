# File: characters_to_numbers.py
# This program converts a textual message into a sequence of Unicode numbers.

def main():
    print("This program converts a textual message into a sequence of numbers to represent the Unicode encoding of the message.\n")

    # Type the textual message to encode.
    inMessage = input("Please enter the textual message to encode: ")

    print("\nHere are the Unicode numbers: ⮧")

    # Process the textual message into Unicode numbers.
    for characterString in inMessage:
        # Convert the characters into Unicode numbers and print the result.
        print(ord(characterString), end = " ")

    # This line is the end of the output.
    print()

main()