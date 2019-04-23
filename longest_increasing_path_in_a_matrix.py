class Solution: # TLE, based on pacific atlantic water flow blog
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        
        n = len(matrix[0])
        m = len(matrix)
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(i,j, visited):
            visited[i][j] = 1
            path = 0
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                    continue
                else:
                    path = max(path, dfs(x,y,visited))
            # print(i,j,visited, path, matrix[i][j])
            return path + 1
        
        l = 0
        
        for r in range(m):
            for c in range(n):
                visited = [[False for _ in range(n)] for __ in range(m)]
                # print(l, r, c, "start", matrix[r][c])
                l = max(l, dfs(r,c,visited))
                # print(l, r, c, "end", matrix[r][c])
        return l

# memoizing above solution, 324 ms, faster than 70% submissions
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        
        n = len(matrix[0])
        m = len(matrix)
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = [[-1 for _ in range(n)] for __ in range(m)]
        
        def dfs(i,j):
            path = 0
            if visited[i][j] != -1:
                return visited[i][j]
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]: # note that it doesnt matter here if node was already visited
                    continue
                else:
                    path = max(path, dfs(x,y))
            # print(i,j,visited, path, matrix[i][j])
            visited[i][j] = path+1
            return path + 1
        
        l = 0
        for r in range(m):
            for c in range(n):
                # print(l, r, c, "start", matrix[r][c])
                l = max(l, dfs(r,c))
                # print(l, r, c, "end", matrix[r][c])
        return l