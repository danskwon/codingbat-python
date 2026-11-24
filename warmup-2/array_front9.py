# Warmup-2: Exercise 1: array_front9
# Problem Description: Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
# Solved? yes with claude
# Mistakes: 1) return inside the loop. The function ended on the first number, so it never checked the rest. [1, 9, 3] returned False. 2) Reaching for shorthand before the long version worked. You tried to fit the whole answer into one return, which is what produced mistake 1.
# Improvements: in checks membership: 9 in nums[:4] is the shorthand version, once the loop version works. Long version first, then shorthand. Same order as every problem so far.

def array_front9(nums):
    #return 9 in nums[:4]   # short-hand
    for num in nums[:4]:
        if num == 9:
            return True
        return False



if __name__ == "__main__":
    assert array_front9([1, 2, 9, 3, 4]) == True, "array_front9([1, 2, 9, 3, 4]) should be True"
    assert array_front9([1, 2, 3, 4, 9]) == False, "array_front9([1, 2, 3, 4, 9]) should be False"
    assert array_front9([1, 2, 3, 4, 5]) == False, "array_front9([1, 2, 3, 4, 5]) should be False"
    print("All tests passed")
