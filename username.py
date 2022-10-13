# File: username.py
# This script is a simple program that processes strings to generate usernames.

def main():
    print("This program generates computer usernames.\n")

    # Get the user's first and last names.
    firstname = input("Please enter your first name (all lowercase letters): ")
    lastname = input("Please enter your last name (all lowercase letters): ")

    # Concatenate the first initial with seven characters of the last name.
    username = firstname[0] + lastname[:7]

    # Output the username.
    print("\nYour computer username is:", username)

main()