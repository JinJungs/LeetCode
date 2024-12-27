from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        if not coins:
            return -1

        d = dict()
        d[0] = 0

        for a in range(1,amount+1):
            result = float("inf")
            for coin in coins:
                if a >= coin:
                    result = min(result, d[a-coin]+1)
            d[a] = result

        return -1 if (not d[amount] or d[amount] == float("inf")) else d[amount]

        # d[11]
        # d[11-5] + 1 = d[6]+1 = d[1]+2 or d[5]+ 2
        # d[11-2] + 1 = d[9]+1
        # d[11-1] + 1 = d[10]+1

        # d[1-1] + 1 = d[0]+1 = 1
        # d[2] = min(d[2-1] + 1, d[2-2]+1)
        # d[5] = min(min(d[5-5] + 1, d[5-2]+ 1), d[5-1]+1)

