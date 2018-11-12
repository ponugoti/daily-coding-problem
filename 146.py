# October 20, 2018

"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and
return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def swap_twos(head):
    if head is None:
        return None
    if head.next is None:
        return head

    swapped = listify(head)
    for i in range(0, len(swapped), 2):
        try:
            swapped[i], swapped[i+1] = swapped[i+1], swapped[i]
        except IndexError:
            break

    return nodify(swapped)


def nodify(arr):
    return Node(arr[0], nodify(arr[1:]) if len(arr) > 1 else None)


def listify(head):
    data = []
    while head is not None:
        data.append(head.data)
        head = head.next
    return data


if __name__ == '__main__':
    test_data = (
        (Node(1), [1]),
        (Node(1, Node(2, Node(3, Node(4)))), [2, 1, 4, 3]),
        (Node(1, Node(2, Node(3, Node(4, Node(5))))), [2, 1, 4, 3, 5])
    )

    for nodes, expected in test_data:
        assert listify(swap_twos(nodes)) == expected
