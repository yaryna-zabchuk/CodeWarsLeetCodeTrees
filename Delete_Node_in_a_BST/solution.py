'''
Solution for LeetCode problem 450: Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/description/
'''

from collections import deque

class TreeNode:
    '''Node class for binary tree'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''Solution class for deleting a node in a binary search tree'''
    def deleteNode(self, root, key):
        '''Delete a node from a binary search tree'''
        cur = root
        parent = None

        while cur and cur.val != key:
            parent = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right 

        if not cur:
            return None

        elif not cur.left and not cur.right:
            if parent is None:
                return None
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        
        elif not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if parent is None:
                return child

            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        
        elif cur.left and cur.right:
            min_node = cur.right
            while min_node.left:
                min_node = min_node.left

            cur.val = min_node.val
            cur.right = self.deleteNode(cur.right, min_node.val)

        return root
