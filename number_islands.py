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
            

# 48ms, faster than 99% solutions, https://leetcode.com/problems/number-of-islands/ 
# Credits - LeetCode
from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.grid = None
        self.sets = None
        self.parent = [0]
    
    def find(self, k):
        i = k
        while self.parent[i] != i:
            i = self.parent[i]
        self.parent[k] = i
        return i
    
    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        self.parent[i] = j
        return j
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        self.grid = grid
        sets = self.sets = [[0]*m for i in range(n)]
        
        sequence = 1
        cur = [0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    cur[j] = 0
                    continue
                
                left = cur[j-1] if j > 0 else 0
                top = cur[j]
                if not left and not top:
                    cur[j] = sequence
                    self.parent.append(sequence)
                    sequence += 1
                elif left and not top:
                    cur[j] = left
                elif not left and top:
                    cur[j] = top
                else:
                    cur[j] = self.union(left, top)
        
        return sum(1 for i in range(1, len(self.parent)) if self.parent[i] == i)
        