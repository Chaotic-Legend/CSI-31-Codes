# Isaac D. Hoyos
# Review For Test 1: Question 3

def points():
    for x in range(-4, 2):
        for y in range(-5, 1):
            if y <= x:
                print((x, y), end = "\n")

points()

print()

def main():
    for x in range(5):
        for y in range(6):
            if x <= y:
                print((x, y), end = " ")
        
main()
