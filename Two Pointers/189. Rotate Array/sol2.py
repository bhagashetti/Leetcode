class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        left = 0
        right = n-1
        k = k %n
        while left < right:
            nums[left] ,nums[right] =  nums[right] , nums[left] 
            left+=1
            right-=1
        left = k
        right = n-1
        while left < right:
            nums[left] ,nums[right] =  nums[right] , nums[left] 
            left+=1
            right-=1
        left = 0
        if k < n:
            right = k-1
        else:
            right = n-1
        while left < right:
            nums[left] ,nums[right] =  nums[right] , nums[left] 
            left+=1
            right-=1

