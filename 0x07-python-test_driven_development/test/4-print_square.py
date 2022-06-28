4-print_square.py
=================

    >>> print_square = __import__('4-print_square').print_square

    >>> print_square(5)
    #####
    #####
    #####
    #####
    #####

    >>> print_square(None)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(-5)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0

    >>> print_square(5 + 5)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########

    >>> print_square("Holberton")
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(1, 5)
    Traceback (most recent call last):
        ...
    TypeError: print_square() takes 1 positional argument but 2 were given

    >>> print_square(0)
    >>>

    >>> print_square(a)
    Traceback (most recent call last):
        ...
    NameError: name 'a' is not defined

    >>> print_square(5.2)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
