from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _parse(self, node: TreeNode) -> str:
        if not node:
            return None
        return node.val
    
    def _traverse(self, root: TreeNode) -> List[TreeNode]:
        queue = [root]
        queue_log = [self._parse(root)]
        while queue:
            node = queue.pop()
            if node:
                queue.extend([node.left, node.right])
                queue_log.extend([self._parse(node.left), self._parse(node.right)])
        return queue_log
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_traversal = self._traverse(p)
        q_traversal = self._traverse(q)
        
        for p_node, q_node in zip(p_traversal, q_traversal):
            if p_node != q_node:
                return False
        return True
        