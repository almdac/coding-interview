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
    def isValidBST(self, root: Optional[TreeNode], low=-INF, high=INF) -> bool:
        if not root:
            return True
        if root <= low or root >= high:
            return False
        return self.isValidBST(root.left, low, root) and self.isValidBST(root.right, root, high)