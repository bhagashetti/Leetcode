class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq  = 0
        count =1 
        if len(nums) == 0:
            return 0
        s = set(nums)
        for num in s:
            if num-1 not in s:
                count = 1
                ele  = num
                while ele +1 in s:
                    count+=1
                    ele +=1
                if count > max_seq:
                    max_seq = count 
        return max_seq
