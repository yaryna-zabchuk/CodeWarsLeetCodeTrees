from collections import deque

class Node:
    def __init__(self, data, lefy=None, right=None):
        self.data = data
        self.left = lefy
        self.right = right

# Pre-order traversal
def pre_order(node):
    stack = deque()
    cur = node
    res = []

    while cur or stack:
        if cur:
            res.append(cur.data)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()

    return res

# In-order traversal
def in_order(node):
    stack = deque()
    res = []
    cur = node

    while cur or stack:

        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        res.append(cur.data)
        cur = cur.right

    return res

# Post-order traversal
def post_order(node):
    stack = deque()
    res = []
    cur = node
    last_visited = None

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                cur = peek_node.right
            else:
                res.append(peek_node.data)
                last_visited = stack.pop()

    return res
