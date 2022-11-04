# File: userfile.py
# This program creates a file of usernames in batch mode.

def main():
    print("This program creates a file of usernames from a file of names.\n")

    # Enter the file names.
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # Open the files.
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # Process each line of the input file.
    for line in infile:
        # Get the first and last names from the line variable.
        first, last = line.split()
        # Create the username.
        username = (first[0] + last[:7]).lower()
        # Write it to the output file.
        print(username, file = outfile)

    # Close both files.
    infile.close()
    outfile.close()

    print("\nUsernames have been written to the file:", outfileName)

main()