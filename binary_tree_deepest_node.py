# Find the deepest node of a binary tree

from __future__ import annotations

class BinaryTreeNode:
    def __init__(self, val: int, left: BinaryTreeNode, right: BinaryTreeNode) -> None:
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root: BinaryTreeNode) -> None:
        self.root = root

    def height(self, node: BinaryTreeNode):
        if not node:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return max(left_height, right_height) + 1

    def get_node_at(self, node: BinaryTreeNode, height: int):
        if not node:
            return
        if height == 1:
            return node
        
        left = self.get_node_at(node.left, height-1)
        right = self.get_node_at(node.right, height-1)

        if left:
            return left
        if right:
            return right
    
    def get_deepest_node(self):
        height = self.height(self.root)
        deepest_node = self.get_node_at(height)
        return deepest_node
        

        
        

