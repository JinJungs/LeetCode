from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        """
        1 4 5
        2 7 6
        6 8 7
        """

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = min((float("inf") if j == 0 else dp[i][j-1]), (float("inf") if i == 0 else dp[i-1][j])) + grid[i][j]
        return dp[-1][-1]