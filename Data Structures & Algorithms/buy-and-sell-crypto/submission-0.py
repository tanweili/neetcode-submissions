class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 0, 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[buy]:
                sell = i
                profit = max(profit, (prices[sell] - prices[buy]))
            else:
                buy, sell = i, i
        return profit