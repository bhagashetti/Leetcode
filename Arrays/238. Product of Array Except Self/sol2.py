class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        n = len(nums)
        product = 1
        for num in nums:
            product*=num
            result.append(product)
        product = 1
        for i in range(n-1,-1,-1):
            product *= nums[i]
            nums[i] = product
        nums.append(1)
        result.pop()
        nums.pop(0)

        for i in range(n):
            nums[i] = nums[i] * result[i]
        return nums
       

       