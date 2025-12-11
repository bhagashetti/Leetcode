class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p_sum = 0
        d = {0:1}
        n = len(nums)
        count = 0
        for i in range(n):
            p_sum+=nums[i]
            val = p_sum - k
            if val in d:
                count+=d[val]
            d[p_sum] = 1+d.get(p_sum,0)
        return count