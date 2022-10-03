# Isaac D. Hoyos
# Review For Test 1: Question 4

def main():
    m = float(input("Please enter a numeric value for the slope of the line: "))
    b = float(input("Please enter a numeric value for the y-intercept: "))
    print("The equation of this line is y =", m, "x +", b)

main()

print()

# This script asks the user for the value of the x and y coordinate at two different points and then returns the value for the slope of the line.
def main():
    x1, y1 = eval(input("Please enter the value of the x and y coordinate for the first point separated by a comma: "))
    x2, y2 = eval(input("Please enter the valus of the x and y coordinate for the second point separated by a comma: "))
    if x2 != x1:
        m = (y2 - y1) / (x2 - x1)
        print("The slope of this line is", m)
    else:
        print("This line is vertical with the equation x =", x1)

main()

print()

# This script asks the user for the value of the x and y coordinate at two different points and then returns the equation of the line passing through those two points.
def main():
    x1, y1 = eval(input("Please enter the value of the x and y coordinate for the first point separated by a comma: "))
    x2, y2 = eval(input("Please enter the value of the x and y coordinate for the second point separated by a comma: "))
    if x2 != x1:
        m = (y2 - y1)/(x2 - x1)
        print("The slope of this line is", m)
        b = y1 - m * x1
        print("The equation of this line is y =", m, "x +", b)
    else:
        print("This line is vertical with the equation x =", x1)

main()