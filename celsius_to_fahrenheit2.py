# File: celsius_to_fahrenheit.py
# This program converts Celsius temperature to Fahrenheit. This script version will give you heat and cold warnings.

def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32
    print("\nThe temperature is", round(fahrenheit, 3), "degrees Fahrenheit.")

    # Print warnings for extreme temperatures.
    if fahrenheit > 90:
        print("It's hot out there, so stay hydrated!")
    if fahrenheit < 30:
        print("It's cold out there, so dress warmly!")

main()