# Isaac D. Hoyos
# Review For Test 1: Question 6

def main():
    title = "United States of America"
    print("Our string is:", title)
    print("The amount of characters in our string is:", len(title))
    print("The last character in our string is:", title[-1])
    print("The index of the last character is:", len(title)-1)
    print("The America part can be obtained by doing:", title[17:24])
    L = list(title)
    L.reverse()
    backTitle = "".join(L)
    print("The title in reverse order can be obtained by doing:", backTitle)
    newTitle = title[23] + title[1:23] + title[0]
    print("The first and last characters interchanged gives:", newTitle)

main()