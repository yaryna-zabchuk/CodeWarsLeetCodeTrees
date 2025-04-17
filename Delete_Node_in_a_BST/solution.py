from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
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
