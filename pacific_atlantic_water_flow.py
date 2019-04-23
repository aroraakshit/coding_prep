class Solution(object): # 196ms, Credits -  https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []
        
        for i in range(m):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n-1, a_visited, m, n)
        for j in range(n):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m-1, j, a_visited, m, n)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result
                
                
    def dfs(self, matrix, i, j, visited, m, n):
        # when dfs called, meaning its caller already verified this point 
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)

# 104ms, Credits: leetcode: same idea, launch DFS from two edges per ocean, amazing design!
class Solution:
    def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        
        if not matrix:
            return []

        r = len(matrix)
        c = len(matrix[0])
        visitedP = [[False]*c for i in range(r)]
        visitedA = [[False]*c for i in range(r)]
        

        stackP=[]
        stackA=[]
        for i in range(c):
            stackP.append([0,i])
            stackA.append([r-1,i])
        for i in range(1,r):
            stackP.append([i,0])
        for i in range(r-1):
            stackA.append([i,c-1])
            
        
        while(stackP):
            i,j = stackP.pop()
            visitedP[i][j]=True
            if((i+1)<r and matrix[i][j]<=matrix[i+1][j] and not visitedP[i+1][j]):
                stackP.append([i+1,j])
            if((i-1)>=0 and matrix[i][j]<=matrix[i-1][j] and not visitedP[i-1][j]):
                stackP.append([i-1,j])
            if((j+1)<c and matrix[i][j]<=matrix[i][j+1] and not visitedP[i][j+1]):
                stackP.append([i,j+1])
            if((j-1)>=0 and matrix[i][j]<=matrix[i][j-1] and not visitedP[i][j-1]):
                stackP.append([i,j-1])
                
        while(stackA):
            i,j = stackA.pop()
            visitedA[i][j]=True
            if((i+1)<r and matrix[i][j]<=matrix[i+1][j] and not visitedA[i+1][j]):
                stackA.append([i+1,j])
            if((i-1)>=0 and matrix[i][j]<=matrix[i-1][j] and not visitedA[i-1][j]):
                stackA.append([i-1,j])
            if((j+1)<c and matrix[i][j]<=matrix[i][j+1] and not visitedA[i][j+1]):
                stackA.append([i,j+1])
            if((j-1)>=0 and matrix[i][j]<=matrix[i][j-1] and not visitedA[i][j-1]):
                stackA.append([i,j-1])
                
        outlist=[]
        for i in range(r):
            for j in range(c):
                if visitedP[i][j] and visitedA[i][j]:
                    outlist.append([i,j])
                    
        return outlist