class Solution: # 32ms, Credits - LeetCode, mathy!
    def myPow(self, x: 'float', n: 'int') -> 'float':
        if n == 0:
            return 1.0
        curr_x = x if n>0 else 1/x
        
        extra, ex_mult = 1, 1.0
        n = abs(n)
        while(n>1):
            extra = n%2
            n = n//2
            ex_mult = extra*curr_x*ex_mult if extra else ex_mult
            curr_x *= curr_x
        return ex_mult * curr_x