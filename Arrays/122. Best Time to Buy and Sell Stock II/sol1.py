class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        i = 0
        while i < n-1:
            buy = prices[i]
            j = i+1
            if buy > prices[j]:
                buy = prices[j]
                i+=1
            else:
                max_profit += prices[j] - buy
                i+=1
        return max_profit



        