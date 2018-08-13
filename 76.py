# August 11, 2018

"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing
subsequence in the array. The subsequence does not necessarily have
to be contiguous.

For example, given the array
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6:
it is 0, 2, 6, 9, 11, 15.

[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
"""

# TRY RECURSIVE IMPLEMENTATION
def longest_contiguous(ints):
    def count_longest(lst, base):
        count = 1
        for n in lst:
            if n > base:
                count += 1
                base = n
            print("count:", count, "n:", n, "base:", base)
        return count
    longest = 0
    for i, n in enumerate(ints):
        current = longest
        print("outer:", ints[i:])
        for j, _ in enumerate(ints[i:]):
            print("inner:", ints[j:])
            count = count_longest(ints[j:], n)
            current = max(current, count)
            print("current:", current)
        longest = max(current, longest)

    return longest

if __name__ == '__main__':
    test = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert longest_contiguous(test) == 6
