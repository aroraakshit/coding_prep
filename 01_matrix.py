import sys
class Solution:
    def updateMatrix(self, m: List[List[int]]) -> List[List[int]]:
        r = len(m)
        if r == 0:
            return m
        c = len(m[0])
        d = [ [sys.maxsize for j in range(c)] for i in range(r) ]
        
        for i in range(r):
            for j in range(c):
                if m[i][j] == 0:
                    d[i][j] = 0
                else:
                    if i > 0:
                        d[i][j] = min(d[i][j], d[i-1][j] + 1)
                    if j > 0:
                        d[i][j] = min(d[i][j], d[i][j-1] + 1)
        
        for i in reversed(range(r)):
            for j in reversed(range(c)):
                if m[i][j] == 0:
                    d[i][j] = 0
                else:
                    if i < r-1:
                        d[i][j] = min(d[i][j], d[i+1][j] + 1)
                    if j < c-1:
                        d[i][j] = min(d[i][j], d[i][j+1] + 1)
        
        return d