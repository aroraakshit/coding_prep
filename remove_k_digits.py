import sys
class Solution: # TLE, Recursive solution with memoization, only passes 22/33 cases
    def __init__(self):
        self.d = {}
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        elif k==0:
            return num
        else:
            if num not in self.d:
                res = sys.maxsize
                for i in range(len(num)):
                    res = min( res, int(self.removeKdigits(num[:i]+num[i+1:], k-1)) )
                self.d[num] = str(res)
            return self.d[num]

import sys
class Solution: # 36ms, Credits- LeetCode, stack based solution! to ensure monotonically decreasing sequence! Greedy Algorithm
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i, n in enumerate(num):
            while stack and k and stack[-1]>n: # monotonically decreasing sequence creation!
                    stack.pop()
                    k -= 1
            stack.append(n)    
            if not k:
                break
        
        for _ in range(k):
            stack.pop()
            
        #print(i, stack, k)  
        result = "".join(stack) + num[i+1:]
        result = result.lstrip('0')        
        
        return result if len(result) else '0'