from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h2 = ListNode(None, l2) # Add a dummie head to l2
        p1, p2 = l1, h2
        while p2.next and p1:
            if p2.next.val >= p1.val:
                # Save next l1 node
                next_p1 = p1.next
                # Insert l1 node after l2 node           
                p1.next = p2.next
                p2.next = p1
                # Move l2 pointer to new inserted node
                p2 = p2.next
                # Move l1 pointer to next l1 node
                p1 = next_p1
            else:
                # move l2 pointer
                p2 = p2.next
        while p1:
            # Append remaining of l1 in l2
            p2.next = p1
            p2 = p2.next
            p1 = p1.next
        return h2.next