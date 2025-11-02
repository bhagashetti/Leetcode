class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        result = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                result[j][n-i-1] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]