 # May 31, 2018

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which
serializes the tree into a string, and deserialize(s), which
deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def helper(node, lvl=0):
        if not node:
            return ''
        seperator = '*-' + str(lvl) + '-*'
        left = helper(node.left, lvl+1)
        right = helper(node.right, lvl+1)
        return str(node.val) + seperator + left + seperator + right

    return helper(root)

def deserialize(s):
    def helper(st, lvl=0):
        node = st.split('*-' + str(lvl) + '-*')
        try:
            val, left, right = node[0], node[1], node[2]
        except IndexError:
            # the tree has been travesed exhaustively
            return None
        return Node(val, helper(left, lvl+1), helper(right, lvl+1))

    return helper(s)

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    # root*-0-*left*-1-*left.left*-2-**-2-**-1-**-0-*right*-1-**-1-*
    # print('serialized:', serialize(node))

    assert deserialize(serialize(node)).left.left.val == 'left.left'