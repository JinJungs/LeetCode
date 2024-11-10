# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        nodeList = []

        if not root:
            return result

        nodeList.append(root)
        result.append([root.val])

        while nodeList:
            r = []
            nextNodeList = []
            for node in nodeList:
                if node.left:
                    nextNodeList.append(node.left)
                    r.append(node.left.val)
                if node.right:
                    nextNodeList.append(node.right)
                    r.append(node.right.val)
            if r:
                result.append(r)
            nodeList = nextNodeList

        return result
