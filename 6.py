# June 2, 2018

"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns
the first and last element of that pair.
For example, car(cons(3, 4)) returns 3,and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def _tuplify(a, b):
    return (a, b)

def car(pair):
    a, _ = pair(_tuplify)
    return a

def cdr(pair):
    _, b = pair(_tuplify)
    return b

if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4