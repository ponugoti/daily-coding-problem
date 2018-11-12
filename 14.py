# June 10, 2018

"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring
with k distinct characters is "bcb".
"""

def k_distinct(s, k):
    best_so_far = ''
    for i, _ in enumerate(s):
        cs = s[i:]  # disregard head character in each iteration
        best, distinct = '', set()

        for c in cs:
            best = best + c
            distinct.add(c)
            if len(distinct) is k:
                break

        if len(best) > len(best_so_far):
            best_so_far = best

    return best_so_far


if __name__ == '__main__':
    print(k_distinct('abcba', 2))
