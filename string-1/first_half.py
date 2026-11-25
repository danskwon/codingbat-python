# Warmup-2: Exercise 1: first_half
# Problem Description: Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
# Solved?
# Mistakes: Used / for the midpoint. In Python 3, / always returns a float (6 / 2 = 3.0), and slice indices must be integers, so it raises a TypeError.
# Improvements: Use // (integer division) so the index is always a whole number. It works in both CodingBat's older Python and modern Python 3.
# Use Cases: Splitting text or a list in half, like a preview of the first half of an article or dividing data into two groups.

def first_half(str):
    return str[:len(str) // 2]  # use // for integer division vs / for float division


if __name__ == "__main__":
    assert first_half('WooHoo') == 'Woo', "first_half('WooHoo') should be 'Woo'"
    assert first_half('HelloThere') == 'Hello', "first_half('HelloThere') should be 'Hello'"
    assert first_half('abcdef') == 'abc', "first_half('abcdef') should be 'abc'"
    print("All tests passed")
