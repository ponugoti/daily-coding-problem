# August 7, 2018

"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7
(inclusive) with uniform probability, implement a function rand5()
that returns an integer from 1 to 5 (inclusive).
"""

from random import uniform

def rand7():
    return uniform(1, 7)

def rand5():
    return uniform(1, 5)

if __name__ == '__main__':
    for _ in range(100000):
        assert 1 <= rand7() <= 7
        assert 1 <= rand5() <= 5
