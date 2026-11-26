# Warmup-2: Exercise 1: combo_string
# Problem Description: Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
# Solved?
# Mistakes: else caught two different cases (b shorter, and a tie) under one answer.
#           A tie needs a+b+a, not b+a+b.
# Improvements: Use <= instead of < so the tie case falls into the "a wraps" branch,
#               which happens to give the right answer for both.
# Use Cases: Wrapping a short label around longer content, like padding a filename
#            with a fixed prefix/suffix tag: short_tag + content + short_tag.

def combo_string(a, b):
    if len(a) <= len(b):
        return a + b + a
    return b + a + b


if __name__ == "__main__":
    assert combo_string('Hello', 'hi') == 'hiHellohi', "combo_string('Hello', 'hi') should be 'hiHellohi'"
    assert combo_string('hi', 'Hello') == 'hiHellohi', "combo_string('hi', 'Hello') should be 'hiHellohi'"
    assert combo_string('aaa', 'b') == 'baaab', "combo_string('aaa', 'b') should be 'baaab'"
    print("All tests passed")
