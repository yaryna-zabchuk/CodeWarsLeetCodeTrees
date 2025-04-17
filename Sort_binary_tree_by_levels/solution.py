from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node is None:
        return []

    q = deque()
    q.append(node)
    res = []

    while q:

        cur = q.popleft()
        res.append(cur.value)

        q.append(cur.left) if cur.left else None
        q.append(cur.right) if cur.right else None

    return res
