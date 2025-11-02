class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                red+=1
            elif nums[i] == 1:
                white+=1
            elif nums[i] == 2:
                blue+=1
        for i in range(red):
            nums[i] = 0
        for j in range(red,red+white):
            nums[j] =1
        for k in range(red+white, red+white+blue):
            nums[k] = 2
        
        