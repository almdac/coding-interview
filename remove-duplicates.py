from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        while pointer:
            next_node = pointer.next
            while next_node:
                # Found different
                if next_node.val != pointer.val:
                    pointer.next = next_node
                    next_node = None
                # Found end of list
                elif not next_node.next:
                    pointer.next = None
                    next_node = None
                else:
                    next_node = next_node.next
            # Pointer may be set to None in previous loop
            if pointer:
                pointer = pointer.next
        return head