"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    # break the string into a word list
    # add words one by one (plus a space in between) to a new line of string 
    # until the line length exceeds limit 
    # repeat until word list becomes empty 
    # print all the lines

    word_list = string.split()

    while word_list:

        new_line = ""

        new_line = word_list.pop(0) + " "

        while word_list and len(new_line) + len(word_list[0]) <= limit:
            
            new_line = new_line + word_list.pop(0) + " "

        print(new_line[:-1])



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ALL TESTS PASSED!\n')
