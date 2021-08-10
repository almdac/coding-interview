# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self._order = []
        
    def inorderTraversal(self, root: list[TreeNode]) -> list[int]:
        if not root:
            return
        self.inorderTraversal(root.left)
        self._order.append(root.val)
        self.inorderTraversal(root.right)
        return self._order
        