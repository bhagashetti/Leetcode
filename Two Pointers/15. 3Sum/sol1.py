class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res =[]
        nums = sorted(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1 
            right = n-1
            target = 0-nums[i]
            while left < right:
                val = nums[left] + nums[right]
                if val > target:
                    right-=1
                elif val < target:
                    left+=1
                else:
                    temp = []
                    temp=[nums[i],nums[left],nums[right]]
                    res.append(temp)
                    
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                        
        return res


        