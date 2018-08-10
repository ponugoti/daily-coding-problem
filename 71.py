# August 6, 2018

"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should
return 28.
"""

def nth_perfect(n):
    return (n * 10) + (10 - n)

if __name__ == '__main__':
    test_data = [
        (1, 19),
        (2, 28),
        (7, 73)
    ]
    for n, expected in test_data:
        assert nth_perfect(n) is expected
