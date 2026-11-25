# Warmup-2: Exercise 1: without_end
# Problem Description: Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
# Solved? Yes
# Mistakes: None. The solution is correct.
# Improvements: Replace len(str)-1 with -1. Negative indexes count from the end, so str[1:-1] means "skip the first and last character." Shorter and a common Python idiom.
# Use Cases: Stripping wrapper characters from text, like removing the quotes from '"hello"' or the brackets from "[value]".

def without_end(str):
    # return str[1:len(str) - 1]  # len(str) - 1 isn't necessary when you can just grab the last character with -1
    return str[1:-1]


if __name__ == "__main__":
    assert without_end('Hello') == 'ell', "without_end('Hello') should be 'ell'"
    assert without_end('java') == 'av', "without_end('java') should be 'av'"
    assert without_end('coding') == 'odin', "without_end('coding') should be 'odin'"
    print("All tests passed")
