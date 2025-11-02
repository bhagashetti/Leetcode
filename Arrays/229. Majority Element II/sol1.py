class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        result = []
        for num in nums:
            d[num] = 1+ d.get(num,0)
        for key in d:
            if d[key] > n//3:
                result.append(key)
        return result

