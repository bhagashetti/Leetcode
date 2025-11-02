class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        from collections import deque

        d = deque()
        n = len(nums)

        for i in range(n):
            if d and d[0] == i-k:
                d.popleft()
            while q and nums[i] >= nums[d[-1]]:
                d.pop()
            d.append(i)
            if i >= k-1:
                res.append(nums[d[0]])
    return res
