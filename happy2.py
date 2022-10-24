# File: happy2.py
# This program outputs the happy birthday song using value-returning functions.

def happy():
    return "Happy birthday to you!\n"

def verseFor(person):
    lyrics = happy() * 2 + "Happy birthday, dear " + person + ".\n" + happy()
    return lyrics

def main():
    for person in ["Isaac", "Jakub", "Sidney"]:
        print(verseFor(person))

main()