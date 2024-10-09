from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        num = 0
        q = [root]

        while q:
            r = q.pop()
            num += 1
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)

        return num
