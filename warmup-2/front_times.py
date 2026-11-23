# Warmup-2: Exercise 1: front_times
# Problem Description: Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
# Solved? Yes
# Mistakes: None
# Improvements: None

def front_times(str, n):
    return str[:3] * n


if __name__ == "__main__":
    assert front_times('Chocolate', 2) == 'ChoCho', "front_times('Chocolate', 2) should be 'ChoCho'"
    assert front_times('Chocolate', 3) == 'ChoChoCho', "front_times('Chocolate',) should be 'ChoChoCho'"
    assert front_times('Abc', 3) == 'AbcAbcAbc', "front_times('Abc', 3) should be 'AbcAbcAbc'"
    print("All tests passed")
