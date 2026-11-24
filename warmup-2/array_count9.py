# Warmup-2: Exercise 1: array_count9
# Problem Description: Given an array of ints, return the number of 9's in the array.
# Solved? Yes with help from Claude
# Mistakes: mixed two loops styles together. for num in nums → use num directly and for i in range(len(nums)) → use nums[i]
# Improvements: understand loops better and the for loop styles

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


if __name__ == "__main__":
    assert array_count9([1, 2, 9]) == 1, "array_count9([1, 2, 9]) should be 1"
    assert array_count9([1, 9, 9]) == 2, "array_count9([1, 9, 9]) should be 2"
    assert array_count9([1, 9, 9, 3, 9]) == 3, "array_count9([1, 9, 9, 3, 9]) should be 3"
    print("All tests passed")
