# File: fahrenheit_to_celsius.py
# A program to convert Celsius temperature to Fahrenheit.

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature?"))
    celsius = 5 * (fahrenheit - 32) / 9
    print("The temperautre is", celsius, "degrees Celsius.")

main()
