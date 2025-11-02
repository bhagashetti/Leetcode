class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        visited = set()
        def makeZeros(row,col):
            for i in range(rows):
                var = str(i) + "-" + str(col)
                if matrix[i][col] !=0 and str not in visited:
                    visited.add(var) 
                    matrix[i][col] = 0
            for j in range(cols):
                var = str(row) + "-" + str(j)
                if matrix[row][j] !=0 and var not in visited:
                    visited.add(var) 
                    matrix[row][j] = 0

        for i in range(rows):
            for j in range(cols):
                var = str(i) + "-" + str(j)
                if matrix[i][j] == 0 and var not in visited :
                    visited.add(var)
                    print(i,j)
                    makeZeros(i,j)