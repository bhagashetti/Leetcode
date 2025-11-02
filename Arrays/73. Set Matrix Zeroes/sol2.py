class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        set_rows = set()
        set_cols = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    set_rows.add(i)
                    set_cols.add(j)
        for row in set_rows:
            for j in range(cols):
                matrix[row][j] = 0
        for col in set_cols:
            for i in range(rows):
                matrix[i][col] = 0
        