# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

nums = [10, 15, 3, 7]
k = 17

from itertools import combinations

# First, find the combinations of all the number in the given list
combinations = list(combinations(nums, 2))  # [(10, 15), (10, 3), ..., (3, 7)]
print(combinations)

# Then, check if any of the two numbers sums to k
print(any(sum(c) is k for c in combinations))
