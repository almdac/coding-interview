from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        # Get length of the list
        n = 0
        pointer = head
        while pointer:
            n += 1
            pointer = pointer.next
        
        # Cut the new sub list head from original list
        cut_point = n-(k%n)-1
        i=0
        pointer = head
        new_head = None
        while pointer:
            if i == cut_point:
                new_head = pointer.next
                pointer.next = None
            i += 1
            pointer = pointer.next
        # Rotated to the same old head
        if not new_head:
            return head
        
        # Attatch the new head to the beginning of the list
        pointer = new_head
        join_point = None
        while pointer:
            if not pointer.next:
                join_point = pointer
            pointer = pointer.next
        join_point.next = head
            
        return new_head