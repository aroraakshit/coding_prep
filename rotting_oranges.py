from collections import deque
class Solution: #60ms, nice yield keyword use
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        fresh_indices = []
        rotten_indices = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: 
                    fresh_indices.append([i,j])
                elif grid[i][j] == 2:
                    rotten_indices.append([i,j])
        
        if fresh_indices == []:
            return 0
        elif rotten_indices == []:
            return -1
        
        ans = 0
        
        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    yield nr, nc
                    
        queue = collections.deque([(r,c,0) for r,c in rotten_indices])
        
        while queue:
            r,c,d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if [nr,nc] in fresh_indices:
                    del fresh_indices[fresh_indices.index([nr,nc])]
                    queue.append((nr,nc,d+1))
                    ans = max(ans, d+1)
            if fresh_indices == []:
                return ans
        return -1

