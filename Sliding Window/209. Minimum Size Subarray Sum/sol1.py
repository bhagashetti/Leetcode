class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j =0
        n = len(nums)
        min_length = float('inf')
        sum = 0
        while j < n:
            sum+=nums[j]
            while sum >= target:
                sum -=nums[i]
                min_length = min(j - i + 1,min_length)
                i+=1
                
            j+=1
        
        if min_length == float('inf') :
            return 0
        else:
            return min_length


        