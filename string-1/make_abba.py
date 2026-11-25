# Warmup-2: Exercise 1: make_abba
# Problem Description: Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
# Solved? Yes
# Mistakes: none
# Improvements:

def make_abba(a, b):
    return a + b + b + a


if __name__ == "__main__":
    assert make_abba('Hi', 'Bye') == 'HiByeByeHi', "make_abba('Hi', 'Bye') should be 'HiByeByeHi'"
    assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo', "make_abba('Yo', 'Alice') should be 'YoAliceAliceYo'"
    assert make_abba('What', 'Up') == 'WhatUpUpWhat', "make_abba('What', 'Up') should be 'WhatUpUpWhat'"
    print("All tests passed")
