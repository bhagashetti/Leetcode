class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0
        profit = 0
        l,r = 0 ,1
        n = len(prices)
        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maximum_profit = max(maximum_profit,profit)
                r+=1
            else:
                l = r
                r+=1
        return maximum_profit
