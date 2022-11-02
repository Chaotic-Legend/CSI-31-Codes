# File: dateconvert.py
# This program converts the date format of "mm/dd/yyyy" to the "month day, year" format.

def main():
    # Enter the date.
    dateString = input("Enter a date (mm/dd/yyyy): ")

    # Split the date into components.
    monthString, dayString, yearString = dateString.split("/")

    # Convert the variable monthString to the month name.
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthname = months[int(monthString) - 1]

    # Output the result in the "month day, year" date format.
    print("\nThe converted date is:", monthname, dayString + ",", yearString)

main()