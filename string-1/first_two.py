# Warmup-2: Exercise 1: first_two
# Problem Description: Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
# Solved? Yes
# Mistakes:
# Improvements: slicing already handles short strings so the if statement wasn't needed
# Use Cases: making short codes or previews from longer text, like taking the first letters of a name for initials or truncating a title for display.

def first_two(str):
    #if len(str) < 2:  # the if isn't needed. When the string has fewer than 2 characters, str[:2] returns whatever is there, which is exactly what your if does by hand
    #    return str
    return str[:2]


if __name__ == "__main__":
    assert first_two('Hello') == 'He', "first_two('Hello') should be 'He'"
    assert first_two('abcdefg') == 'ab', "first_two('abcdefg') should be 'ab'"
    assert first_two('ab') == 'ab', "first_two('ab') should be 'ab'"
    print("All tests passed")
