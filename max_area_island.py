class Solution(object): # 112ms
    def maxAreaOfIsland(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        ma = 0
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] == 0 or (i,j) in seen:
                    continue
                # print(i,j,"\n")
                ca = 0
                q = [(i,j)]
                while q!=[]:
                    # print(q, seen, ca)
                    (x,y) = q[0]
                    del q[0]
                    if (x,y) not in seen and  g[x][y] == 1:
                        ca += 1
                        seen.add((x,y))
                        if x+1 < len(g) and (x+1,y) not in seen:
                            q.append((x+1,y))
                        if y+1 < len(g[0]) and (x,y+1) not in seen:
                            q.append((x,y+1))
                        if x-1 >= 0 and (x-1,y) not in seen:
                            q.append((x-1,y))
                        if y-1 >= 0 and (x,y-1) not in seen:
                            q.append((x,y-1))
                ma = max(ma, ca)
        return ma


# 68ms solution, Credits: LeetCode
class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            cnt = 1
            grid[x][y] = 0
            
            if x > 0 and grid[x - 1][y] == 1:
                cnt += dfs(x - 1, y)
            if x + 1 < m and grid[x + 1][y] == 1:
                cnt += dfs(x + 1, y)
            if y > 0 and grid[x][y - 1] == 1:
                cnt += dfs(x, y - 1)
            if y + 1 < n and grid[x][y + 1] == 1:
                cnt += dfs(x, y + 1)
            
            return cnt
        
        cnts = [dfs(x, y) for x in range(m) for y in range(n) if grid[x][y] == 1]
        
        return max(cnts) if cnts else 0
                    