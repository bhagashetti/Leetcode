class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_count = 0
        count = 1
        n = len(nums)
        if n==0:
            return 0

        for i in range(n-1):
            if nums[i] == nums[i+1]-1:
                count+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                max_count = max(count,max_count)
                count = 1
        return max(max_count,count)

        