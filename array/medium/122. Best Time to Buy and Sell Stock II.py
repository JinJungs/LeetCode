from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # how to decide when to sell?
        minBuy = max(prices)
        profit = 0
        for i in range(len(prices)):
            price = prices[i]
            # if next value is lower than price, must sell
            if i > 0 and i < len(prices) -1:
                if price > prices[i+1]:
                    profit += max(0, price - minBuy)
                    minBuy = price
            minBuy = min(minBuy, price)

        profit += prices[-1]- minBuy
        return profit if profit>0 else 0