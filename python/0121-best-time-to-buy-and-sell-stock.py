from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            min_price = min(min_price, sell)
            profit = max(profit, sell - min_price)
        return profit
