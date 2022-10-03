# Isaac D. Hoyos
# Review For Test 1: Question 5

def main():
    a = float(input("Enter the value for a in the quadratic equation ax^2 + bx + c: "))
    b = float(input("Enter the value for b in the quadratic equation ax^2 + bx + c: "))
    c = float(input("Enter the value for c in the quadratic equation ax^2 + bx + c: "))
    x = float(input("Enter the value for x to evaluate: "))
    print()
    print("The function of your parabola is f(x) =", a, "x^2 +", b, "x +", c)
    f = (a * (x**2) + b * x + c)
    print("The evaluation at x =", x, "is f(", x, ") =", f)

main()