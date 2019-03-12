import pprint 
# doesnt work on : [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
class Solution(object):
    def __init__(self):
        self.d_up = {}
        self.d_down = {}
        
    def cherryPickupHelper(self, x, y, g, num_cherries, goingDown):
        # pprint.pprint(g)
        # print("\n\n")
        
        if x >= len(g) or y >= len(g) or x<0 or y<0 or g[x][y] == -1:
            return 0
        
        if g[x][y] == 1:
            num_cherries += 1
            g[x][y] = 0
        
        if goingDown:
            if x == len(g)-1 and y == len(g)-1:
                return max(self.cherryPickupHelper(x-1, y, g, num_cherries, False), self.cherryPickupHelper(x, y-1, g, num_cherries, False))
            else:
                if (x, y) not in self.d_down:
                    self.d_down[(x,y)] = max(self.cherryPickupHelper(x+1, y, g, num_cherries, True), self.cherryPickupHelper(x, y+1, g, num_cherries, True))
                return self.d_down[(x,y)]
        else: # going up!
            if x == 0 and y == 0:
                return num_cherries
            else:
                if (x,y) not in self.d_up:
                    self.d_up[(x,y)] = max(self.cherryPickupHelper(x-1, y, g, num_cherries, False), self.cherryPickupHelper(x, y-1, g, num_cherries, False))
                return self.d_up[(x,y)]
        
    
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        elif len(grid) == 1:
            return int(grid[0][0] == 1)
        return self.cherryPickupHelper(0, 0, grid, 0, True)


class Solution(object): #Credits: LeetCode
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        memo = [[[None] * N for j in range(N)] for k in range(N)]
        
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (r1 == N or r2 == N or c1 == N or c2 == N or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return - sys.maxint + 1
            elif r1 == c1 == N - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2]:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1+1, c1, c2+1),
                           dp(r1, c1+1, c2+1),
                           dp(r1+1, c1, c2),
                           dp(r1, c1+1, c2))
            memo[r1][c1][c2] = ans
            return ans
            
            
        return max(0, dp(0,0,0))