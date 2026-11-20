# Logic-1: Exercise 8: in1to10
# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
# Solved. Mistakes:  . Improvements:  .s

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    return 1 <= n <= 10


if __name__ == "__main__":
    assert in1to10(5, False) == True, "in1to10(5, False) should be True"
    assert in1to10(11, False) == False, "in1to10(11, False) should be False"
    assert in1to10(11, True) == True, "in1to10(11, True) should be True"
    print("All tests passed")
