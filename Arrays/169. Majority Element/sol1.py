class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        half = n//2

        dict = {}
        for i in range(n):
            if nums[i] in dict:
                dict[nums[i]] +=1
            else:
                dict[nums[i]] = 1
            if dict[nums[i]] > half:
                return nums[i]
                
        