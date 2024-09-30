# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], sums: int):
            if not root:
                return False

            sums += root.val
            if not root.left and not root.right:
                return sums == targetSum

            return dfs(root.left, sums) or dfs(root.right, sums)

        if not root:
            return False

        return dfs(root, 0)
