# Logic-1: Exercise 1: near_ten
# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
# Solved. Mistakes: Read the problm incorrectly and gave the wrong solution.
# Improvements: slow down on the wording
# Cleanup: For a non-negative number, num % 10 is always between 0 and 9. So 0 <= and <= 9 can never be False, and you can remove num % 10 <= 2 or num % 10 >= 8

def near_ten(num):
    last_digit = num % 10
    return last_digit <= 2 or last_digit >= 8


if __name__ == "__main__":
    assert near_ten(12) == True, "near_ten(12) should be True"
    assert near_ten(17) == False, "near_ten(17) should be False"
    assert near_ten(19) == True, "near_ten(19) should be True"
    print("All tests passed")
