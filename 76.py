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

def longest_contiguous(arr):

    def helper(base, items):
        if not items:
            return 0
        head = items[0]
        tail = items[1:] if len(items) > 1 else None
        count = 1 if head > base else 0
        base = max(base, head)
        # print('b:', base, 'h:', head, 'c:', count)
        return count + helper(base, tail)

    # Convert this to work recursively
    longest = 0
    for i in arr:
        for j in range(len(arr)):
            current = longest
            tail = arr[j:]
            for _ in range(len(tail)):
                print('helper(' + str(i) + ', ' + str(tail) + ')')
                current = max(current, helper(i, tail))
                print('current:', current)
            longest = max(longest, current)
            print('longest:', longest)

    print('final:', longest, '\n')
    return longest

if __name__ == '__main__':
    test = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert longest_contiguous(test) == 6
