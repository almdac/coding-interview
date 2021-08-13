# https://leetcode.com/problems/minimum-depth-of-binary-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if left_depth and right_depth:
            return min(left_depth, right_depth) + 1
        elif left_depth:
            return left_depth + 1
        elif right_depth:
            return right_depth + 1
        else:
            return 1