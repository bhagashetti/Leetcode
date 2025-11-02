class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}
        left = 0
        n = len(nums)
        if k >= n :
            for i in range(n):
                if nums[i] in seen:
                    return True
                seen[nums[i]] = i
        seen = {}
        for i in range(n-k):
            seen = {}
            for j in range(i,i+k+1):
                if nums[j] in seen:
                    return True
                seen[nums[j]] = j
        return False

        