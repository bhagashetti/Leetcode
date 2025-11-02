class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet_sum = float('inf')
        best_diff = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - curr_sum)
                if diff < best_diff:
                    best_diff = diff
                    closet_sum = curr_sum
                if curr_sum > target :
                    right-=1
                else:
                    left+=1
        return closet_sum
        