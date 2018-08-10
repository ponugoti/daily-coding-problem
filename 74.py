# August 9, 2018

"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

def reverse(node):
    pass

if __name__ == '__main__':
    linked_list = Node(4, Node(3, Node(2, Node(1, Node(0)))))
    reversed_list = reverse(linked_list)

    for test_val in range(5):
        assert reversed_list.val == test_val
        reversed_list = reversed_list.nxt

