# Warmup-2: Exercise 1: string_times
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
# Solved? Yes
# Mistakes: No
# Improvements: none

def string_times(str, n):
    return str * n


if __name__ == "__main__":
    assert string_times('Hi', 2) == 'HiHi', "string_times('Hi', 2) should be 'HiHi'"
    assert string_times('Hi', 3) == 'HiHiHi', "string_times('Hi', 3) should be 'HiHiHi'"
    assert string_times('Hi', 1) == 'Hi', "string_times('Hi', 1) should be 'Hi'"
    print("All tests passed")
