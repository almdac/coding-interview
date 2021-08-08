from __future__ import annotations
from typing import Optional
from math import inf as INF

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __le__(self, node: TreeNode) -> bool:
        return self.val <= node.val

    def __le__(self, val: int) -> bool:
        return self.val <= val
    
    def __ge__(self, node: TreeNode) -> bool:
        return self.val >= node.val

    def __ge__(self, val: int) -> bool:
        return self.val >= val

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stack = [(root, -INF, INF)]
        while len(stack) > 0:
            node, low, high = stack.pop()
            if not node:
                continue
            if node <= low or node >= high:
                return False
            stack.append((node.right, node, high))
            stack.append((node.left, low, node))
        return True