# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(h1: Optional[TreeNode], h2: Optional[TreeNode]) -> bool:
            if not h1 and not h2:
                return True
            if (h1 and not h2) or (h2 and not h1):
                return False
            if h1.val != h2.val:
                return False
            return isSame(h1.left, h2.left) and isSame(h1.right, h2.right)
        return isSame(p,q)
