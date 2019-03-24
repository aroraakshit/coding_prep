
# Idea - repeat number_islands_2.py for every position
import copy # TLE
class UnionFind():
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.parent = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.parent.append(i*n+j)
                else:
                    self.parent.append(-1)
        self.rank = [0 for i in range(m*n)]
        self.count = sum([sum([1 if grid[i][j] == '1' else 0 for j in range(len(grid[i]))]) for i in range(len(grid))])
        
    def find(self, i):
        # print(i, self.parent)
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if(rootx != rooty):
            if (self.rank[rootx] > self.rank[rooty]):
                self.parent[rooty] = rootx
            elif( self.rank[rootx] < self.rank[rooty] ):
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
    
    def get_count(self):
        return self.count
class Solution:
        
    def numIslands2(self, m,n,positions):
        if(positions == []):
            return [1]
        nr = m
        nc = n
        origgrid = [ [0 for i in range(n)] for j in range(m) ]
        op = []
        for row,column in positions:
            origgrid[row][column] = '1'
            grid = copy.deepcopy(origgrid)
            union = UnionFind(grid)
            for r in range(nr):
                for c in range(nc):
                    if grid[r][c] == '1':
                        grid[r][c] = '0'
                        if (r-1>=0 and grid[r-1][c] == '1'):
                            # union[r*nc+c].add((r-1)*nc+c)
                            union.union(r*nc+c, (r-1)*nc+c)
                        if (r+1<nr and grid[r+1][c] == '1'):
                            # union[r*nc+c].add((r+1)*nc+c)
                            union.union(r*nc+c, (r+1)*nc+c)
                        if (c-1>=0 and grid[r][c-1] == '1'):
                            # union[r*nc+c].add(r*nc+c-1)
                            union.union(r*nc+c, r*nc+c-1)
                        if (c+1<nc and grid[r][c+1] == '1'):
                            # union[r*nc+c].add(r*nc+c+1)
                            union.union(r*nc+c, r*nc+c+1)
            op.append(union.get_count())
        return op

# 948ms, Union Find
import copy
class UnionFind():
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.parent = [-1 for i in range(m*n)]
        self.rank = [0 for i in range(m*n)]
        self.count = 0
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if(rootx != rooty):
            if (self.rank[rootx] > self.rank[rooty]):
                self.parent[rooty] = rootx
            elif( self.rank[rootx] < self.rank[rooty] ):
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
    
    def get_count(self):
        return self.count
class Solution:
        
    def numIslands2(self, m,n,positions):
        if(positions == []):
            return []
        elif len(positions) == 1:
            return [1]
        
        nr = m
        nc = n
        grid = [ ['0' for i in range(n)] for j in range(m) ]
        union = UnionFind(grid)
        op = []
        for r,c in positions:
            overlap = []
            if (r-1>=0 and union.parent[(r-1)*nc+c] > -1):
                overlap.append((r-1)*nc+c)
            if (r+1<nr and union.parent[((r+1)*nc+c)] > -1):
                overlap.append((r+1)*nc+c)
            if (c-1>=0 and union.parent[(r*nc+c-1)] > -1):
                overlap.append(r*nc+c-1)
            if (c+1<nc and union.parent[r*nc+c+1] > -1):
                overlap.append(r*nc+c+1)
            union.parent[r*nc+c] = r*nc+c
            union.count += 1
            for i in overlap:
                union.union(i, r*nc+c)
            op.append(union.get_count())
        return op

# 176ms, Credits - LeetCode, basic idea is union find
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parents = [-1 for i in range(m * n)]
        count = 0
        result = []
        for x, y in positions:
            index = x * n + y
            parents[index] = index
            count += 1
            if x >= 1 and parents[index - n] != -1:
                r1, r2 = self.find(parents, index - n), parents[index]
                if r1 != r2:
                    count -= 1
                parents[r1] = r2
            if x < m - 1 and parents[index + n] != -1:
                r1, r2 = self.find(parents, index + n), parents[index]
                if r1 != r2:
                    count -= 1
                parents[r1] = r2
            if y >= 1 and parents[index - 1] != -1:
                r1, r2 = self.find(parents, index - 1), parents[index]
                if r1 != r2:
                    count -= 1
                parents[r1] = r2
            if y < n - 1 and parents[index + 1] != -1:
                r1, r2 = self.find(parents, index + 1), parents[index]
                if r1 != r2:
                    count -= 1
                parents[r1] = r2
            result.append(count)
        return result            
        
    def find(self, parents, index):
        if parents[index] == index:
            return index
        parents[index] = self.find(parents, parents[index])
        return parents[index]
    