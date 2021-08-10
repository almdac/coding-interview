# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: list[TreeNode]) -> list[int]:
        order = []
        stack = [root]
        node = root
        while node or stack:
            if node is not None:
                stack.append(node.left)
                node = node.left
            elif stack:
                node = stack.pop()
                if node:
                    order.append(node.val)
                    stack.append(node.right)
                    node = node.right
        return order