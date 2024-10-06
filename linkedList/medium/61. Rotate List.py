# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        tail = ListNode()
        cnt = 0
        now = head

        while now:
            cnt += 1
            if not now.next:
                tail = now
                break
            now = now.next

        remain = k if k < cnt else k % cnt
        if remain == 0:
            return head

        now2 = head
        cnt2 = 0
        rotate_head = ListNode()
        while now2:
            cnt2 += 1
            if cnt2 == cnt - remain:
                # rotate_head should be now2.next
                rotate_head = now2.next
                # now2.next should be tail
                now2.next = None
                # tail.next should be head
                tail.next = head
                break
            now2 = now2.next

        return rotate_head

