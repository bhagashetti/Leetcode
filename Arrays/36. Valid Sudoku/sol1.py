class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            d = {str(i): 0 for i in range(1, 10)}
            for j in range(cols):
                if board[i][j].isdigit():
                    if d[board[i][j]] == 0:
                        d[board[i][j]] = 1
                    else:
                        return False
        for i in range(cols):
            d = {str(i): 0 for i in range(1, 10)}
            for j in range(rows):
                if board[j][i].isdigit():
                    if d[board[j][i]] == 0:
                        d[board[j][i]] = 1
                    else:
                        return False
        
        for i in range(0,rows,3):
            for j in range(0,cols,3):
                d = {str(i): 0 for i in range(1, 10)}
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l].isdigit():
                            if d[board[k][l]] == 0:
                                d[board[k][l]] = 1
                            else:
                                return False
        return True
                        





        