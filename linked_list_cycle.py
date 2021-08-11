# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        pointer = head
        while pointer:
            if pointer in visited:
                return True
            else:
                visited.add(pointer)
            pointer = pointer.next
