from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        t = len(triangle)
        minpath = [[0 for _ in range(t)] for _ in range(t)]
        q = []

        # insert q
        for i in range(t):
            q.append([t-1, i])

        while q:
            row, index = q.pop()
            value = triangle[row][index]
            if row == t-1:
                minpath[row][index] = value
            else:
                minpath[row][index] = min(minpath[row+1][index], minpath[row+1][index+1]) + value

            print(row, index, minpath[row][index])
            if row != 0 and len(triangle[row-1]) != index:
                q.append([row-1, index])

        return minpath[0][0]