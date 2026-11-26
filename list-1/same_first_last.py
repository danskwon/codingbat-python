# Warmup-2: Exercise 1: same_first_last
# Problem Description: Given an array of ints, return True if the array is
# length 1 or more, and the first element and the last element are equal.
# Mistakes: None. The solution is correct.
# Improvements: None needed. The length check correctly comes first, so an empty
#               list never reaches nums[0] or nums[-1] and can't crash.
# Use Cases: Validating that a sequence isn't empty before checking its endpoints,
#            like confirming a non-empty order history starts and ends on the
#            same product.

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


if __name__ == "__main__":
    assert same_first_last([1, 2, 3]) == False, "same_first_last([1, 2, 3]) should be False"
    assert same_first_last([1, 2, 3, 1]) == True, "same_first_last([1, 2, 3, 1]) should be True"
    assert same_first_last([1, 2, 1]) == True, "same_first_last([1, 2, 1]) should be True"
    print("All tests passed")
