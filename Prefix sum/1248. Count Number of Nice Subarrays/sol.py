class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] % 2==0:
                nums[i] = 0
            else:
                nums[i] = 1
        prefix_sum = 0
        count = 0
        d = {0:1}
        for i in range(n):
            prefix_sum +=nums[i]
            val = prefix_sum - k
            if val in d:
                count+=d[val]
            d[prefix_sum] = 1+ d.get(prefix_sum,0)
        return count
        