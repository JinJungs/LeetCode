# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def merge_sort(head: Optional[ListNode]):
            if not head or not head.next:
                return head

            # find mid node with slow/fast
            slow = head
            fast = head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow

            # cut the node into two
            h1 = head
            h2 = mid.next
            mid.next = None

            m1 = merge_sort(h1)
            m2 = merge_sort(h2)

            # extra node space
            result = ListNode()
            result_head = result
            while m1 and m2:
                if m1.val < m2.val:
                    result_head.next = m1
                    m1 = m1.next
                else:
                    result_head.next = m2
                    m2 = m2.next
                result_head = result_head.next

            # add remain nodes
            if m1:
                result_head.next = m1
            else:
                result_head.next = m2

            return result.next

        # main
        return merge_sort(head)
