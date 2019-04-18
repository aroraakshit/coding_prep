class Solution: # 36ms, Credits- LeetCode
    def gameOfLife(self, board):
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.nnb(board,i,j) == 3:
                        board[i][j] = 2
                else:
                    if self.nnb(board,i,j) < 2 or self.nnb(board,i,j) >3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0

    def nnb(self, board, i, j):
        m,n = len(board), len(board[0])
        count = 0
        if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2
        if i-1 >= 0:                count += board[i-1][j]%2
        if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2
        if j-1 >= 0:                count += board[i][j-1]%2
        if j+1 < n:                 count += board[i][j+1]%2
        if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2
        if i+1 < m:                 count += board[i+1][j]%2
        if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
        return count