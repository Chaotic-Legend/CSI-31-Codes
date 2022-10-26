# File: fahrenheit_to_celsius.py
# This program converts Farenheit temperature to Celsius.

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (5 * (fahrenheit - 32) / 9)
    print("\nThe temperautre is", round(celsius, 4), "degrees Celsius.")

main()
