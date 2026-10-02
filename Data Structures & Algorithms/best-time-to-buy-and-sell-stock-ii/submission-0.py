class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] <= prices[i]:
                profit += prices[i] - prices[buy_idx]
                buy_idx = i + 1
        profit += prices[-1] - prices[buy_idx]
        return profit

