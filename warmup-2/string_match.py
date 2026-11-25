# Warmup-2: Exercise 1: string_match
# Problem Description: Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
# Solved? Yes with Claude
# Mistakes:
# Improvements: learned min() that picks the smaller of two numbers e.g. min(7, 6)   # 6

def string_match(a, b):
    matches = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i+2] == b[i:i+2]:
            matches += 1
    return matches


if __name__ == "__main__":
    assert string_match('xxcaazz', 'xxbaaz') == 3, "string_match('xxcaazz', 'xxbaaz') should be 3"
    assert string_match('abc', 'abc') == 2, "string_match('abc', 'abc') should be 2"
    assert string_match('abc', 'axc') == 0, "string_match('abc', 'axc') should be 0"
    print("All tests passed")
