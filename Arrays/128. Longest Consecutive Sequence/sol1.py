class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq  = 0

        d = {}
        for num in nums:
            d[num] = 1+ d.get(num,0)
        for num in nums:
            count = 1
            while num +1 in d:
                count+=1
                num +=1
            if count > max_seq:
                max_seq = count 
        return max_seq
