# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:
    def bfs(self, node: TreeNode):
        q = [node]
        result = []

        while q:
            result.append(q[0].val)
            temp = []
            for x in q:
                if x.right:
                    temp.append(x.right)
                if x.left:
                    temp.append(x.left)
            q = temp

        return result


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.bfs(root)
