# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(head: Optional[TreeNode]):
            if not head:
                return 1, True
            l, l2= getDepth(head.left)
            r, r2 = getDepth(head.right)
            result = l2 and r2 and abs(l-r) <= 1
            return max(l,r)+1, result

        d, result = getDepth(root)
        return result

