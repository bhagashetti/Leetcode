class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        for num in nums:
            d[num] = 1+d.get(num,0)
        min_heap = []
        for key in d:
            temp = [-d[key],key]
            min_heap.append(temp)
        heapq.heapify(min_heap)
        result =[]
        while k > 0:
            _,val = heapq.heappop(min_heap)
            result.append(val)
            k-=1
        
        return result
        


        