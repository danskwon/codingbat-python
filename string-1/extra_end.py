# Warmup-2: Exercise 1: extra_end
# Problem Description: Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
# Solved? Yes
# Mistakes: none
# Improvements: keep practicing negative indexing

def extra_end(str):
    return str[-2:] * 3


if __name__ == "__main__":
    assert extra_end('Hello') == 'lololo', "extra_end('Hello') should be 'lololo'"
    assert extra_end('ab') == 'ababab', "extra_end('ab') should be 'ababab'"
    assert extra_end('Hi') == 'HiHiHi', "extra_end('Hi') should be 'HiHiHi'"
    print("All tests passed")
