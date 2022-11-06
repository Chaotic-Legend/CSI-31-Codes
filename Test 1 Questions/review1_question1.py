# Isaac D. Hoyos
# Review For Test 1: Question 1

def divisible():
    for i in range(100):
        if (i % 7 == 0) and (i % 3 == 0) and (i % 9 != 0):
            print(i, end = "\n")

divisible()

print()

def main():
    for i in range(0, 100, 21):
        if (i % 9 != 0):
            print(i, end = " ")

main()
