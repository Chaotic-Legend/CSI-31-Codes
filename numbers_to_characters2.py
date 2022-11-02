# File: numbers_to_characters2.py
# This program converts a sequence of Unicode numbers into a string of text. This script is an efficient version using a list accumulator.

def main():
    print("This program converts a sequence of Unicode numbers into the string of text that it represents.\n")

    # Type the Unicode numbers to encode.
    inNumbers = input("Please enter the Unicode numbers of the message: ")
    listOfNumbersEntered = inNumbers.split()

    # Processes the Unicode numbers to print out the string of text.
    characters = []
    for numberString in listOfNumbersEntered:
        # Convert the entered Unicode numbers into integers to plug into another variable.
        codeNumbers = int(numberString)
        # Accumulate the new characters of the message.
        characters.append(chr(codeNumbers))

    message = "".join(characters)
    
    print("\nThe decoded textual message is:", message)

main()