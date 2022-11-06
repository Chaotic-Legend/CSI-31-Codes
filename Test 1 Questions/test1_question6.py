# Isaac D. Hoyos
# Test 1: Question 6

def reverse():
    title = (input("Please enter a word or a number to be the string: "))
    L = list(title)
    L.reverse()
    backTitle = "".join(L)
    print("\nThe string in reverse order can be obtained by doing:", backTitle)

reverse()
