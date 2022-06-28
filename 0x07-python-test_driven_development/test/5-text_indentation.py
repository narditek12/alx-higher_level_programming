5-text_indentation.py
=====================

    >>> text_indentation = __import__('5-text_indentation').text_indentation

    >>> text_indentation(None)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

    >>> text_indentation()
    Traceback (most recent call last):
        ...
    TypeError: text_indentation() missing 1 required positional argument: 'text'

    >>> text_indentation(1)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

    >>> text_indentation("Hello:Holberton?School")
    Hello:
    <BLANKLINE>
    Holberton?
    <BLANKLINE>
    School
