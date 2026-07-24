class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        max_prof = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            elif prices[sell] > prices[buy]:
                prof = prices[sell] - prices[buy]
                if prof > max_prof: 
                    max_prof = prof
            sell += 1

        return max_prof
