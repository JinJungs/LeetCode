import copy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def nvlVal(n: Optional[ListNode]) -> int:
    return 0 if n == None else n.val

def nvlNext(n: Optional[ListNode]) -> ListNode:
    return None if n == None else n.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        answer = ListNode()
        currentNode = answer
        carry = 0

        # currentNode.value = l1.val + l2.val
        # currentNode.next = newNode() set value if sum of the value exceed 10
        # currentNode = newNode

        ### I missed when carry !=0 !!
        while l1!= None or l2 != None or carry !=0:
            # calculate
            sumVal = nvlVal(l1) + nvlVal(l2) + carry
            digit = sumVal % 10
            carry = sumVal // 10

            # set next
            newNode = ListNode(digit)
            currentNode.next = newNode
            currentNode = newNode

            # move next
            l1 = nvlNext(l1)
            l2 = nvlNext(l2)

        ### I missed this point!!
        return answer.next