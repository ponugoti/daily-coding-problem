# June 6, 2018

"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest
sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6,
and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def largest_non_adj_sum(data):
    pass

if __name__ == '__main__':
    test_data = [
        ([2, 4, 6, 2, 5], 13),            # 2 + 6 + 5
        ([5, 1, 1, 5], 10),               # 5 + 5
        ([0, 2, -4, 3, -2, 4, 7, -1], 12) # 2 + 3 + 7
    ]
    for ints, expected in test_data:
        assert largest_non_adj_sum(ints) is expected