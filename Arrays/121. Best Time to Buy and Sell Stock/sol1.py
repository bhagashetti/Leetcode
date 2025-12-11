class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 1:
            return 0
        profit = 0
        buy = prices[0]
        maximum_profit = 0
        for i in range(1,n):
            sell = prices[i]
            profit = sell - buy
            if profit > maximum_profit:
                maximum_profit = profit
            if buy > prices[i]:
                buy = prices[i]
        return maximum_profit
                



        