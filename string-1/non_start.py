# Warmup-2: Exercise 1: non_start
# Problem Description: Given 2 strings, return their concatenation, except
# omit the first char of each. The strings will be at least length 1.
# Mistakes: None. The solution is correct.
# Improvements: None needed. This is already the cleanest version.
# Use Cases: Stripping a known prefix character before combining two pieces of data,
#            like dropping a leading currency symbol or flag character from each
#            of two fields before joining them.

def non_start(a, b):
    return a[1:] + b[1:]


if __name__ == "__main__":
    assert non_start('Hello', 'There') == 'ellohere', "non_start('Hello', 'There') should be 'ellohere'"
    assert non_start('java', 'code') == 'avaode', "non_start('java', 'code') should be 'avaode'"
    assert non_start('shotl', 'java') == 'hotlava', "non_start('shotl', 'java') should be 'hotlava'"
    print("All tests passed")
