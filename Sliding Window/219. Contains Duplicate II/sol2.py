class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}
        n = len(nums)
        for i in range(k+1):
            if i <= n-1:
                if nums[i] in seen:
                    return True
                seen[nums[i]] = i
        left = 0
        for i in range(k+1,n):
            del seen[nums[left]]
            if nums[i] in seen:
                return True
            seen[nums[i]] = i
            left+=1

        return False

        