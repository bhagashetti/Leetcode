class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1 for i in range(n)]
        for i in range(1,n):
            left[i] = nums[i-1] * left[i-1]
        right = [1 for i in range(n)]
        for j in range(n-2,-1,-1):
            right[j] = right[j+1] * nums[j+1]
        output = [1 for i in range(n)]
        for i in range(n):
            output[i] = left[i] * right[i]
        return output
        
        