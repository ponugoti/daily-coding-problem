# Recursive staircase problem


def num_ways_with_2p(n, x):
    """The num of ways the steps can be legally taken."""
    if n is 0 or n is 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a+b
    return b


def num_ways_with_xp(n, x):
    if n < 0:
        return 0
    if n is 0 or n is 1:
        return 1
    ways = [1, None]
    for i in range(1, n):
        total = 0
        for j in x:
            if i-j >= 0:
                total += ways[i-j]
        ways[i] = total
    return ways[n]


if __name__ == '__main__':
    n = 2       # num of stairs
    x = (1, 2)  # legal step permutations

    print(num_ways_with_2p(n, x))
