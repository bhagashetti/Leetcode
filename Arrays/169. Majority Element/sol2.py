class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        element = None
        n = len(nums)
        for i in range(n):
            if count == 0:
                element = nums[i]
                count = 1
            elif nums[i] == element:
                count+=1
            else:
                count-=1
        return element   