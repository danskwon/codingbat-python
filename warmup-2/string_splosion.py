# Warmup-2: Exercise 1: string_splosion
# Problem Description: Given a non-empty string like "Code" return a string like "CCoCodCode".
# Solved? Used Claude
# Mistakes: learned to use start/stop with range(start, stop) in accumulator patter
# Improvements:

def string_splosion(str):
    result = ''
    for i in range(1, len(str) + 1):
        result += str[:i]
    return result


if __name__ == "__main__":
    assert string_splosion('Code') == 'CCoCodCode', "string_splosion('Code') should be 'CCoCodCode'"
    assert string_splosion('abc') == 'aababc', "string_splosion('abc') should be 'aababc'"
    assert string_splosion('ab') == 'aab', "string_splosion('ab') should be 'aab'"
    print("All tests passed")
