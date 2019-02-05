class Solution: # 76ms
    def mark(self, grid, visited, i, j):
        # print(i,j)
        if(j<0 or \
           i<0 or \
           i >=len(visited) or \
           j>=len(visited[i]) or \
           visited[i][j] or \
           grid[i][j] != '1'):
            return
        visited[i][j] = 1
        self.mark(grid, visited, i, j+1)
        self.mark(grid, visited, i-1, j)
        self.mark(grid, visited, i, j-1)
        self.mark(grid, visited, i+1, j)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j]==0 and grid[i][j] == '1':
                    num_islands += 1
                    self.mark(grid, visited, i, j)
        return num_islands

# 56 ms approach (credits - leetcode)
# class Solution:
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if grid is None:
#             return 0
        
#         count = 0
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     count += 1
#                     self.dfs(i,j,grid)
                    
#         return count
    
#     def dfs(self, i,j, grid):
#         grid[i][j] = '0'
        
#         if i-1>=0 and grid[i-1][j] == '1':
#             self.dfs(i-1,j,grid)
            
#         if i + 1 < len(grid) and grid[i+1][j] == '1':
#             self.dfs(i+1, j, grid)
            
#         if j -1 >= 0 and grid[i][j-1] == '1':
#             self.dfs(i, j-1, grid)
        
#         if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
#             self.dfs(i , j+1, grid)
            