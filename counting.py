# File: counting.py
# This program counts the words and characters in a textual message.

def main():
    inText = input("Enter your textual message: ")
    NumberOfCharacters = len(inText)
    NumberOfWords = len(inText.split())
    print()
    print(inText.split("\n"))
    print("\nThis textual message has {0} character(s) and {1} word(s).".format(NumberOfCharacters, NumberOfWords))

main()