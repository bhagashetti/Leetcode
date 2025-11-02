class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        min_heap = nums 
        heapq.heapify(min_heap)
        n = len(nums)
        diff = n-k
        while diff:
            heapq.heappop(min_heap)
            diff-=1
        return min_heap[0]

        
        