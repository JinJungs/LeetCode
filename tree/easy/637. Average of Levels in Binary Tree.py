# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = []
        q = [[0,root]]
        while q:
            depth, v = q.pop()
            if depth <= len(d) - 1:
                arr = d[depth]
                arr.append(v.val)
                d[depth] = arr
            else:
                arr = []
                arr.append(v.val)
                d.append(arr)

            if v.left:
                q.append([depth+1, v.left])
            if v.right:
                q.append([depth+1, v.right])

        result = []
        for arr in d:
            result.append(sum(arr) / len(arr))

        return result
