# Warmup-2: Exercise 1: first_last6
# Problem Description: Given an array of ints, return True if 6 appears as
# either the first or last element in the array. The array will be length 1 or more.
# Mistakes: None. The solution is correct.
# Improvements: None needed. Already the cleanest version.
# Use Cases: Checking the endpoints of a sequence, like confirming a transaction
#            log starts or ends with a specific status code.

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6


if __name__ == "__main__":
    assert first_last6([1, 2, 6]) == True, "first_last6([1, 2, 6]) should be True"
    assert first_last6([6, 1, 2, 3]) == True, "first_last6([6, 1, 2, 3]) should be True"
    assert first_last6([13, 6, 1, 2, 3]) == False, "first_last6([13, 6, 1, 2, 3]) should be False"
    print("All tests passed")
