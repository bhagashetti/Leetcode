class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for x ,y in points:
            val = x ** 2 + y**2
            temp = [val,[x,y]]
            distance.append(temp)
        heapq.heapify(distance)

        result = []

        while k > 0:
            _ , val = heapq.heappop(distance)
            result.append(val)
            k-=1
       
        return result

        