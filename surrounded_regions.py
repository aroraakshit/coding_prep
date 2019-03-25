class Solution: # 120ms, 
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board): return

        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        # print(save)
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
                print(board)
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]

class Solution: #96ms, Credits - LeetCode, BFS based
    # start bfs on boundary 'O's, mark them and then change every other O to X, and markers to O
    def solve(self, board):
        def bfs(board, i, j):
            m=len(board)
            n=len(board[0])
            curLevel=set([(i,j)])
            board[i][j]='A'

            while curLevel:
                nextLevel=set()
                for i, j in curLevel:
                    if i-1>=0 and board[i-1][j]=='O':
                        nextLevel.add((i-1, j))
                        board[i-1][j]='A'
                    if i+1<=m-1 and board[i+1][j]=='O':
                        nextLevel.add((i+1, j))
                        board[i+1][j]='A'

                    if j-1>=0 and board[i][j-1]=='O':
                        nextLevel.add((i, j-1))
                        board[i][j-1]='A'

                    if j+1<=n-1 and board[i][j+1]=='O':
                        nextLevel.add((i, j+1))
                        board[i][j+1]='A'
                curLevel=nextLevel

        if not board:
            return
        m=len(board)
        n=len(board[0])
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j]=='O':
                    bfs(board, i ,j)

        for j in [0, n-1]:
            for i in range(m):
                if board[i][j]=='O':
                    bfs(board, i ,j)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='A':
                    board[i][j]='O'