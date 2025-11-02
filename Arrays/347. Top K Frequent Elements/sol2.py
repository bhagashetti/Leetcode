class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        if k == len(nums):
            return nums

        count = collections.Counter(nums)
        max_heap = []
        heapq.heapify(max_heap)

        for element , frequency in count.items():
            heapq.heappush(max_heap,(-frequency,element))
        while k :
            result.append(heapq.heappop(max_heap)[1])
            k-=1
        return result


    
        

        