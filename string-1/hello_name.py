# Warmup-2: Exercise 1: hello_name
# Problem Description: Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
# Solved?
# Mistakes: print vs return. the function needs to return the string, not print it.
# Improvements:

def hello_name(name):
    return f'Hello {name}!'


if __name__ == "__main__":
    assert hello_name('Bob') == 'Hello Bob!', "hello_name('Bob') should be 'Hello Bob!'"
    assert hello_name('Alice') == 'Hello Alice!', "hello_name('Alice') should be 'Hello Alice!'"
    assert hello_name('X') == 'Hello X!', "hello_name('X') should be 'Hello X!'"
    print("All tests passed")
