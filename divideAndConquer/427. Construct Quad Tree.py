# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        directions = ['topLeft', 'topRight', 'bottomLeft', 'bottomRight']

        def divide(startX:int, endX:int, startY:int, endY:int, dirc: str):
            midX = (startX + endX) // 2
            midY = (startY + endY) // 2
            if dirc == 'topLeft':
                nsx = startX
                nex = midX
                nsy = startY
                ney = midY
            elif dirc == 'topRight':
                nsx = startX
                nex = midX
                nsy = midY + 1
                ney = endY
            elif dirc == 'bottomLeft':
                nsx = midX + 1
                nex = endX
                nsy = startY
                ney = midY
            elif dirc == 'bottomRight':
                nsx = midX + 1
                nex = endX
                nsy = midY + 1
                ney = endY

            return (nsx, nex, nsy, ney)

        def findLeaf(startX, endX, startY, endY):
            if endX - startX == 0:
                return Node(grid[startX][startY] == 1, True, None, None, None, None)

            node = Node(True, False, None, None, None, None)

            for dirc in directions:
                nsx, nex, nsy, ney = divide(startX, endX, startY, endY, dirc)
                newNode = findLeaf(nsx, nex, nsy, ney)

                if dirc == 'topLeft':
                    node.topLeft = newNode
                elif dirc == 'topRight':
                    node.topRight = newNode
                elif dirc == 'bottomLeft':
                    node.bottomLeft = newNode
                elif dirc == 'bottomRight':
                    node.bottomRight = newNode

            # merge
            if (node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val) and (node.topLeft.isLeaf == node.topRight.isLeaf == node.bottomLeft.isLeaf == node.bottomRight.isLeaf == True):
                node.val = node.topLeft.val
                node.isLeaf = True
                node.topLeft = node.topRight = node.bottomLeft = node.bottomRight = None

            return node

        n = len(grid)
        head = findLeaf(0, n-1, 0, n-1)
        return head
