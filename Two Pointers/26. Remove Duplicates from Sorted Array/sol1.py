class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        res = []
        i = 0
        while i < n:
            while i < n-1 and nums[i] == nums[i+1]:
                i+=1
            res.append(nums[i])
            i+=1        
        n = len(res)

        for i in range(n):
            nums[i] = res[i]
        return n