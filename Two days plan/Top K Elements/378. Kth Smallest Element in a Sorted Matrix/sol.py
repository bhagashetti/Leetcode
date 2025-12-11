class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                result.append(matrix[i][j])
        heapq.heapify(result)
        while k > 1:
            heapq.heappop(result)
            k-=1
        return result[0]

