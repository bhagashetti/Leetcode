class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for sell in prices:
            profit = sell-buy
            if sell < buy:
                buy = sell
            if profit > max_profit:
                max_profit = profit
        return max_profit

        
        