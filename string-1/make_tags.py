# Warmup-2: Exercise 1: make_tags
# Problem Description: The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
# Solved? Yes
# Mistakes: none
# Improvements:

def make_tags(tag, word):
    #return '<' + tag + '>' + word + '</' + tag + '>'  # for Python before 3.6 (e.g., CodingBat)
    return f'<{tag}>{word}</{tag}>'

if __name__ == "__main__":
    assert make_tags('i', 'Yay') == '<i>Yay</i>', "make_tags('i', 'Yay') should be '<i>Yay</i>'"
    assert make_tags('i', 'Hello') == '<i>Hello</i>', "make_tags('i', 'Hello') should be '<i>Hello</i>'"
    assert make_tags('cite', 'Yay') == '<cite>Yay</cite>', "make_tags('cite', 'Yay') should be '<cite>Yay</cite>'"
    print("All tests passed")
