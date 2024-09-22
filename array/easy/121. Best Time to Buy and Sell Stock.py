from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = max(prices)

        for i in range(len(prices)):
            price = prices[i]
            minBuy = min(minBuy, price)
            profit = max(profit, price - minBuy)

        return profit if profit > 0 else 0