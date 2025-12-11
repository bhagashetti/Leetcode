class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        buy = prices[0]

        for i in range(1,n):
            sell = prices[i]
            if buy < sell:
                profit = sell - buy
                if profit > max_profit:
                    max_profit  = profit
            if buy > prices[i]:
                buy = prices[i]
        return max_profit


        