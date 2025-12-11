class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums = sorted(nums)
        for i in range(n-3): 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                z = n-1
                while k < z:
                    val = nums[i] + nums[j] + nums[k] + nums[z]
                    if val == target:
                        res.append([nums[i],nums[j],nums[k] , nums[z]])
                        k+=1
                        z-=1
                        while k < z and nums[k] == nums[k-1]:
                            k+=1
                        while k < z and nums[z] == nums[z+1]:
                            z-=1
                        
                    elif val < target:
                        k+=1
                    elif val > target:
                        z-=1
                    
        return res

        