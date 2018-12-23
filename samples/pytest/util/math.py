"""
    Demo of a math lib
"""


def one():
    return 1


def square(x):
    """ Returns squase of an integer input value """
    if isinstance(x, int):
        return x*x
    else:
        raise TypeError


def cube(x):
    """ Returns cube of an integer input value """
    if isinstance(x, int):
        return x*x*x
    else:
        raise TypeError
