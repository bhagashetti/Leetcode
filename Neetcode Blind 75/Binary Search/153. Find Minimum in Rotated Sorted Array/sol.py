class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = -1
        n = len(nums)
        for i in range(n):
            if i != n-1 and nums[i] > nums[i+1]:
                index = i
                break
        result = []
        if index != -1:
            return nums[index+1]
        else:
            return nums[0]