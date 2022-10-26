# File: celsius_to_fahrenheit.py
# This program converts Celsius temperature to Fahrenheit.

def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32
    print("\nThe temperature is", round(fahrenheit, 3), "degrees Fahrenheit.")

main()
