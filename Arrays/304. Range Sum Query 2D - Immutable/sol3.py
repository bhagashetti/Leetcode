class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        for i in range(rows):
            for j in range(1,cols):
                self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i][j]
        for i in range(1,rows):
            for j in range(cols):
                self.matrix[i][j] = self.matrix[i-1][j] + self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        bottom = self.matrix[row2][col2]
        top = self.matrix[row1-1][col2] if row1 > 0 else 0
        leftbottom = self.matrix[row2][col1-1] if col1 > 0 else 0
        lefttop = self.matrix[row1-1][col1-1] if row1 and col1 > 0 else 0

        sum =  bottom - top - (leftbottom - lefttop)
        return sum
        



  
     
        # sum = prefix[row2][col2] - prefix[row1-1][col2]-prefix[row2][col1-1]
        
        return sum
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)