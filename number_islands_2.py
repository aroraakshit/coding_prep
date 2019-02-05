# Using disjoint sets
# Generic implementation: https://github.com/imressed/python-disjoint-set/blob/master/disjoint_set.py 

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
        
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if(grid == []):
            return 0
        nr = len(grid)
        nc = len(grid[0])
        
        union = UnionFind(grid)
        num_islands = 0
        
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
        num_islands = union.get_count()
        return num_islands