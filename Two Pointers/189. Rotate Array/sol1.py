class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while k > 0:
            next = nums[0]   
            for i in range(1,n):
                prev = next
                next = nums[i]
                nums[i] = prev
            nums[0] = next
            k-=1
