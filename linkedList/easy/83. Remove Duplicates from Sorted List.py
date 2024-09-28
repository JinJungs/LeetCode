from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        while head and head.next:
            if head.val == head.next.val:
                nextNode = head.next
                head.next = nextNode.next
                nextNode.next = None
            else:
                head = head.next

        return result