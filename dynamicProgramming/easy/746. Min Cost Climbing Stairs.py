from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        d[n] = min(d[n-1], d[n-2]) + cost[n]
        """
        n = len(cost)
        d = [0 for _ in range(n)]
        d[0] = cost[0]
        d[1] = cost[1]

        for i in range(2,n):
            d[i] = min(d[i-1], d[i-2]) + cost[i]

        return min(d[-1], d[-2])