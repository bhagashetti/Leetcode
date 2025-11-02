class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        for right in range(1,n):
            if nums[left] != nums[right]:
                left+=1
                nums[left] = nums[right]
        return left+1
