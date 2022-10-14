# File: numbers_to_characters.py
# This program converts a sequence of Unicode numbers into a string of text.

def main():
    print("This program converts a sequence of Unicode numbers into a string of text that it represents.\n")

    # Type the Unicode numbers to encode.
    inNumbers = input("Please enter the Unicode numbers of the message: ")
    listOfNumbersEntered = inNumbers.split()

    # Processes the Unicode numbers to print out the string of text.
    message = ""
    for numberString in listOfNumbersEntered:
        # Convert the entered Unicode numbers into integers to plug into another variable.
        codeNumbers = int(numberString)
        # Concatenate the representing characters of the Unicode numbers to the message variable.
        message = message + chr(codeNumbers)
    
    print("\nThe decoded textual message is:", message)

main()