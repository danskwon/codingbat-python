# Warmup-2: Exercise 1: left2
# Problem Description: Given a string, return a "rotated left 2" version where
# the first 2 chars are moved to the end. The string length will be at least 2.
# Mistakes: None. The solution is correct.
# Improvements: None needed. Slicing already handles strings shorter than 2 chars,
#               so no if statement is required.
# Use Cases: Rotating data in a fixed cycle, like moving the first item of a queue
#            to the back, or cycling through a rotation of on-call engineers.

def left2(str):
    return str[2:] + str[:2]


if __name__ == "__main__":
    assert left2('Hello') == 'lloHe', "left2('Hello') should be 'lloHe'"
    assert left2('java') == 'vaja', "left2('java') should be 'vaja'"
    assert left2('Hi') == 'Hi', "left2('Hi') should be 'Hi'"
    print("All tests passed")
