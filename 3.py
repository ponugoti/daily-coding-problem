# May 30, 2018

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element
  at index i of the new array is the product of all the numbers in
  the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
  would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
  expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

ints = [1, 2, 3, 4, 5]

def with_division(arr):
    from operator import mul
    from functools import reduce

    # Get the product of all ints in the list and divide the result
    # with the list element at a given index
    product = reduce(mul, ints)
    return [int(product / i) for i in ints]

def without_division(arr):
    result = [1] * len(arr)
    for idx, elm in enumerate(arr):
        for i in ints:
            if i is not elm:
                result[idx] *= i
    return result

if __name__ == '__main__':
    print(ints)
    print(with_division(ints))
    print(without_division(ints))