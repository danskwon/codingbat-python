# Warmup-2: Exercise 1: make_out_word
# Problem Description: Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
# Solved?
# Mistakes:
# Improvements:

def make_out_word(out, word):
    #return out[:2] + word + out[-2:]  # codingbat runs an older version of Python that doesn't support f-strings
    return f'{out[:2]}{word}{out[-2:]}'


if __name__ == "__main__":
    assert make_out_word('<<>>', 'Yay') == '<<Yay>>', "make_out_word('<<>>', 'Yay') should be '<<Yay>>'"
    assert make_out_word('<<>>', 'WhooHoo') == '<<WhooHoo>>', "make_out_word('<<>>', 'WhooHoo') should be '<<WhooHoo>>'"
    assert make_out_word('[[]]', 'word') == '[[word]]', "make_out_word('[[]]', 'word') should be '[[word]]'"
    print("All tests passed")
