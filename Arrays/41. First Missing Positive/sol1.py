class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        d = {}
        missing_number = None

        for num in nums:
            d[num] = 1+ d.get(num,0)
        n = len(nums)
        print(d)
        for i in range(1,n+1):
            if i not in d:
                missing_number = i
                break
        if not missing_number:
            missing_number = n+1
        return missing_number

        