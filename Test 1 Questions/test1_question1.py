# Isaac D. Hoyos
# Test 1: Question 1

import math
from math import log as ln

def main():
    print("∛2 - ln(π) + cos(e) =", pow(2, 1/3) - ln(math.pi) + math.cos(math.e))
    print("\nThe approximated rounded value of ∛2 - ln(π) + cos(e) is", round(pow(2, 1/3) - ln(math.pi) + math.cos(math.e), 3))

main()
