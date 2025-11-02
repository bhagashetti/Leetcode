class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix_sum = 0
        d = {0:1}
        n = len(nums)
        count = 0
        for i in range(n):
            prefix_sum+=nums[i]
            val = prefix_sum - goal
            if val in d:
                count+=d[val]
            d[prefix_sum] = 1+ d.get(prefix_sum,0)
        return count
