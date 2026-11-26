# Warmup-2: Exercise 1: make_pi
# Problem Description: Return an int array length 3 containing the first 3
# digits of pi, {3, 1, 4}.
# Mistakes: None. There was no logic to get wrong here, the function just
#           returns a fixed list literal.
# Improvements: None needed.
# Use Cases: Returning a constant, known value from a function, like default
#            settings, a fixed list of allowed categories, or starter data
#            for a new record.

def make_pi():
    return [3, 1, 4]


if __name__ == "__main__":
    assert make_pi() == [3, 1, 4], "make_pi(test_args) should be [3, 1, 4]"
    print("All tests passed")
