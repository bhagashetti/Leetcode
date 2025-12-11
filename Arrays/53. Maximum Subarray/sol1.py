class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum = float('-inf')
        sum  = 0
        n = len(nums)
        for i in range(n):
            sum+=nums[i]
            if sum > maximum_sum:
                maximum_sum = sum
            if sum < 0:
                sum = 0
        return maximum_sum
        