# File: celsius_to_fahrenheit.py
# This program converts Celsius temperature to Fahrenheit.

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32
    print("\nThe temperautre is", round(fahrenheit, 3), "degrees Fahrenheit.")

main()
