# Warmup-2: Exercise 1: array123
# Problem Description: Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
# Solved?
# Mistakes: With lists, in checks whether something is one of the items. "return [1, 2, 3] in nums" asks "is the list [1, 2, 3] one of the items in nums?" The items are all numbers, so the answer is always False.
# Improvements:

def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1, 2, 3]:
            return True
        return False


if __name__ == "__main__":
    assert array123([1, 1, 2, 3, 1]) == True, "array123([1, 1, 2, 3, 1]) should be True"
    assert array123([1, 1, 2, 4, 1]) == False, "array123([1, 1, 2, 4, 1]) should be False"
    assert array123([1, 1, 2, 1, 2, 3]) == True, "array123([1, 1, 2, 1, 2, 3]) should be True"
    print("All tests passed")
