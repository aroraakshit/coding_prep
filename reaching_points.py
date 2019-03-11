class Solution: # TLE, dp working backwards
    def __init__(self):
        self.d = {}
        
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        if tx < sx or ty < sy:
            return False
        
        elif tx == sx and ty == sy:
            return True
        
        elif (sx,sy,tx,ty) in self.d:
            return d[(sx,sy,tx,ty)]
        
        elif tx == sx:
            self.d[(sx,sy,tx,ty)] = self.reachingPoints(sx, sy, tx, ty%tx)
            
        elif ty == sy:
            self.d[(sx,sy,tx,ty)] = self.reachingPoints(sx, sy, tx%ty, ty)
        
        else:
            self.d[(sx,sy,tx,ty)] = self.reachingPoints(sx, sy, tx%ty, ty) or self.reachingPoints(sx, sy, tx, ty%tx)
        
        return self.d[(sx,sy,tx,ty)]

class Solution(object): #40ms, iterative modulo variant, working backwards, Credits - LeetCode
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx-sx) % ty == 0
            else: # tx < ty
                if tx > sx:
                    ty %= tx
                else:
                    return (ty-sy) % tx == 0
        return tx == sx and ty == sy