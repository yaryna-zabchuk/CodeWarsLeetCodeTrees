'''
Solution for the problem "Sort binary tree by levels" on CodeWars.
https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python
'''

from collections import deque

class Node:
    '''Node class for binary tree'''
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    '''Sort binary tree by levels'''
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
