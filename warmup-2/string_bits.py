# Warmup-2: Exercise 1: string_bits
# Problem Description: Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
# Solved?
# Mistakes: use a for loop and range function. range() stops one before the number you give it. e.g. range(4) gives 0, 1, 2, 3
# Improvements:

def string_bits(args):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]
    return result

    # alternative code using slicing shortcut
    # return str[::2]  # start at the beginning, go to the end, take every 2nd char

if __name__ == "__main__":
    assert string_bits('Hello') == 'Hlo', "string_bits('Hello') should be 'Hlo'"
    assert string_bits('Hi') == 'H', "string_bits('Hi') should be 'H'"
    assert string_bits('Heeololeo') == 'Hello', "string_bits('Heeololeo') should be 'Hello'"
    print("All tests passed")
