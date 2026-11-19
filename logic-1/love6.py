# Logic-1: Exercise 7: love6
# Problem description: The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
# Solved. Mistake(s) made: none

def love6(a, b):
    total = a + b
    difference = abs(a - b)
    return a == 6 or b == 6 or total == 6 or difference == 6


if __name__ == "__main__":
    assert love6(6, 4) == True, "love6(6, 4) should be True"
    assert love6(4, 5) == False, "love6(4, 5) should be False"
    assert love6(1, 5) == True, "love6(1, 5) should be True"
    print("All tests passed")
