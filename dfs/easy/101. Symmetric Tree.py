from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, left, right):
        # check Emtpry
        if not left and not right:
            return True
        elif not left and right:
            return False
        elif not right and left:
            return False

        # return False if value is different
        if left.val != right.val:
            return False

        return self.isSame(left.right, right.left) and self.isSame(left.left, right.right)
