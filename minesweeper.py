# https://leetcode.com/problems/minesweeper/ 

class Solution:
    
    def neighbors(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        nbrs = []
        # print(m,n,r,c)
        if r+1 < m and c+1 < n:
            nbrs += [[r+1, c+1]]
        if r+1 < m:
            nbrs += [[r+1, c]]
        if r+1 < m and c > 0:
            nbrs += [[r+1, c-1]]
        if c+1 < n:
            nbrs += [[r, c+1]]
        if c > 0:
            nbrs += [[r, c-1]]
        if r > 0 and c > 0:
            nbrs += [[r-1, c-1]]
        if r > 0:
            nbrs += [[r-1, c]]
        if r > 0 and c+1 < n:
            nbrs += [[r-1, c+1]]
        return nbrs
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # print(click)
        r = click[0]
        c = click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        if board[r][c] == 'B':
            return board
        m = len(board)
        n = len(board[0])
        nbrs = self.neighbors(m, n, r, c)
        num_adj_mines = 0
        for nbr in nbrs:
            if board[nbr[0]][nbr[1]] == 'M':
                num_adj_mines += 1
        if num_adj_mines == 0:
            board[r][c] = 'B'
            for nbr in nbrs:
                board = self.updateBoard(board, nbr)
        else:
            board[r][c] = str(num_adj_mines)
        return board