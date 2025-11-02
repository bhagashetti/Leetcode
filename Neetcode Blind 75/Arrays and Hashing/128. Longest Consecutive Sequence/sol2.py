class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_count = 0
        for num in s:
            if num-1 not in s:
                count = 1
                while (num+count) in s:
                    count+=1
                max_count = max(max_count,count)
        return max_count
        
       