# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], l: List[int]):
            if not root:
                return
            l.append(root.val)
            dfs(root.left, l)
            dfs(root.right, l)
        result = []
        dfs(root, result)
        result.sort()

        d = 100000
        for i in range(1,len(result)):
            d = min(d, abs(result[i-1] -result[i]))
        return d