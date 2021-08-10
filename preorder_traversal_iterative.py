# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: list[TreeNode]) -> list[int]:
        order = []
        stack = [root]
        while len(stack):
            node = stack.pop()
            if node:
                order.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return order