# June 1, 2018

"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array can
contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

inputs = [ [3, 4, -1, 1],
           [1, 2, 0] ]

# start with the smallest positive int
smallest = 1

for arr in inputs:

    for i in arr:
        if i is smallest:
            smallest += 1

    # print result and reset for next input set
    print(smallest)
    result = 1