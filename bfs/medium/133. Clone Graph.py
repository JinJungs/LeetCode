"""
# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if not node.neighbors:
            return Node(node.val, None)

        clone_node = Node(node.val, node.neighbors)
        q = deque([clone_node])
        visited = dict()

        while q:
            clone_head = q.popleft()

            if clone_head and clone_head.neighbors:
                new_neighbors = []
                for neighbor in clone_head.neighbors:
                    if neighbor.val not in visited.keys():
                        clone_neighbor = Node(neighbor.val, neighbor.neighbors)
                        new_neighbors.append(clone_neighbor)
                        q.append(clone_neighbor)
                        visited[clone_neighbor.val] = clone_neighbor
                    else:
                        new_neighbors.append(visited[neighbor.val])

                clone_head.neighbors = new_neighbors
                visited[clone_head.val] = clone_head

        return clone_node

