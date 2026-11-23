# Warmup-2: Exercise 1: last2
# Problem Description: Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
# Solved? No
# Mistakes: many. more range() practice and using negative indexing
# Improvements: practice more with looks, slicing and indexing

def last2(str):
    end = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        if str[i:i + 2] == end:
            count += 1
    return count


if __name__ == "__main__":
    assert last2('hixxhi') == 1, "last2('hixxhi') should be 1"
    assert last2('xaxxaxaxx') == 1, "last2('xaxxaxaxx') should be 1"
    assert last2('axxxaaxx') == 2, "last2('axxxaaxx') should be 2"
    print("All tests passed")
