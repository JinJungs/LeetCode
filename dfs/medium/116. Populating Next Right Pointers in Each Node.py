# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root or not root.left:
            return
        # (1) set next for root.left
        root.left.next = root.right

        # (2) set next for root.right
        if root.next != None:
            root.right.next = root.next.left

        self.dfs(root.left)
        self.dfs(root.right)