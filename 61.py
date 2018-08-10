# July 27, 2018

"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be
partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into
{15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since
we can't split it up into two subsets that add up to the same sum.
"""

def split(multiset):
    A, B = set(), set()
    for n in sorted(multiset, reverse=True):
        if sum(A) < sum (B):
            A.add(n)
        else:
            B.add(n)
        print('A:', A)
        print('B:', B)
        print()
    return (A, B)

if __name__ == '__main__':
    ms = [15, 5, 20, 10, 35, 15, 10]
    print(ms)
    print(sorted(ms, reverse=True))
    print(split(ms))