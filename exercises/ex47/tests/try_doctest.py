""" Study Drill 2: 
Learn about Python's 'doc tests', and see if you like them better.

To use doctest, put three greater-than signs in front of the code you
wish to test, followed by the expected output.

>>> greek_letter("alpha")
'α'

Then include the if-statement at the bottom of this module.

To run the test: "$ python try_doctest.py"
If no output, then all the tests passed.
Run "$ python try_doctest.py -v" for verbose output.
"""
import doctest


def greek_letter(english_name):
    """Return the Unicode character for a Greek letter.

    english_name is case-sensitive.
    >>> greek_letter("Alpha") == greek_letter("alpha")
    False

    Must be a Greek letter.
    >>> greek_letter("one")
    Traceback (most recent call last):
    ...
    ValueError: No such Greek letter: one
    """ 
    letters = {"Alpha": "\u0391",
               "alpha": "\u03B1",
               "Beta": "\u0392",
               "beta": "\u03B2"}

    unicode_greek = letters.get(english_name)
    if unicode_greek is None:
        raise ValueError(f"No such Greek letter: {english_name}")
    else:
        return unicode_greek


if __name__ == "__main__":
    doctest.testmod()
