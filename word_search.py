class Solution: # 268 ms
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        
        if len(word) == 0 or len(word) > r*c:
            return False
        
        def dfs(visited, idx, ix, jx):
            if [ix,jx] in visited:
                # print(visited)
                return False
            if idx == len(word)-1:
                return True
            flag = False
            visited.append([ix,jx])
            if ix > 0 and board[ix-1][jx] == word[idx+1]:
                flag = flag or dfs(visited, idx+1, ix-1, jx)
            if ix < r-1 and board[ix+1][jx] == word[idx+1]:
                flag = flag or dfs(visited, idx+1, ix+1, jx)
            if jx > 0 and board[ix][jx-1] == word[idx+1]:
                flag = flag or dfs(visited, idx+1, ix, jx-1)
            if jx < c-1 and board[ix][jx+1] == word[idx+1]:
                flag = flag or dfs(visited, idx+1, ix, jx+1)
            visited.pop()
            return flag
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = []
                    if dfs(visited, 0, i, j) == True:
                        return True
        return False

# if you just add some more quick checks to this solution, like line 41 to 48, it speeds up to 68ms! (Apparently just because of special test cases)
import collections
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        
        bcnts = collections.Counter(c for x in board for c in x)
        
        for c, cnt in collections.Counter(word).items():
            if c not in bcnts or cnt > bcnts[c]:
                return False
            
        r = len(board)
        c = len(board[0])
        
        if len(word) == 0 or len(word) > r*c:
            return False
        
        def dfs(visited, idx, ix, jx):
            if [ix,jx] in visited:
                return False
            if idx == len(word)-1:
                return True
    
            visited.append([ix,jx])
            if ix > 0 and board[ix-1][jx] == word[idx+1]:
                if dfs(visited, idx+1, ix-1, jx):
                    return True
            if ix < r-1 and board[ix+1][jx] == word[idx+1]:
                if dfs(visited, idx+1, ix+1, jx):
                    return True
            if jx > 0 and board[ix][jx-1] == word[idx+1]:
                if dfs(visited, idx+1, ix, jx-1):
                    return True
            if jx < c-1 and board[ix][jx+1] == word[idx+1]:
                if dfs(visited, idx+1, ix, jx+1):
                    return True
            visited.pop()
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = []
                    if dfs(visited, 0, i, j):
                        return True
        return False