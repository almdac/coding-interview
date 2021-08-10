# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: list[TreeNode], order=[]) -> list[int]:
        if not root:
            return
        order.append(root.val)
        self.preorderTraversal(root.left, order)
        self.preorderTraversal(root.right, order)
        return order
