# File: chaos.py
# Our thrid function is a simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function.")
x = eval(input("Enter a number between 0 and 1: " ))
if x > 0 and x < 1:
    for i in range(10):
        x = 3.9 * x * (x-1)
        print(x)

else:
    print("Your number x is out of range.")
    
main()
