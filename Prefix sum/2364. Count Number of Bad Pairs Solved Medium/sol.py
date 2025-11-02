class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total_pairs = 0
        good_pairs = 0
        n = len(nums)
        count = {}
        for i in range(n):
            total_pairs+=i
            good_pairs+=count.get(nums[i]-i,0)
            count[nums[i]-i] = 1+ count.get(nums[i]-i,0)

        return total_pairs - good_pairs
        