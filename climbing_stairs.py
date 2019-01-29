class Solution:
    def __init__(self):
        self.d = {}
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        elif n in self.d: return self.d[n]
        else:
            self.d[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
            return self.d[n]