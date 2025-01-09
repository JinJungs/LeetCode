from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        d = [[0 for _ in range(n)] for _ in range(m)]

        """
        1 1 1
        1 0 0
        1 0 0

        d[i][j] = d[i-1][j] + d[i][j-1]
        """

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    d[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    d[i][j] = 1
                elif i == 0:
                    d[i][j] = d[i][j-1]
                elif j == 0:
                    d[i][j] = d[i-1][j]
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]

        return d[-1][-1]
