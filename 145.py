# October 19, 2018

"""
This problem was asked by Google.

Given an array of numbers and an index i, return the index of the
nearest larger number of the number at index i, where distance is
measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any
one of them. If the array at i doesn't have a nearest larger integer,
then return null.

Follow-up: If you can preprocess the array, can you do this in
constant time?
"""

def nearest_larger_number(arr, idx):
    """
    arr -> array of numbers
    idx -> index of starting number

    return -> the index of the closest largest number
    """
    target = arr[idx]

    for i in range(len(arr)):
        before, after = idx - i, idx + i

        if before >= 0 and arr[before] > target:
            return before

        if after < len(arr) and arr[after] > target:
            return after

    return None


if __name__ == '__main__':
    test_data = (
        ([4, 1, 3, 5, 6], 0, 3),
        ([4, 2, 3, 1, 0, 5], 2, 0)
    )
    for array, idx, expected in test_data:
        assert nearest_larger_number(array, idx) is expected, "failed"