class Solution: # 36ms
    def isValid(self, s: str) -> bool:
        stack = []
        closing = [']','}',')']
        opening = ['[','{','(']
        for i in s:
            if i in closing:
                if stack != [] and opening[closing.index(i)] == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif i in opening:
                stack.append(i)
            else:
                return False
            # print(stack)
        if stack == []:
            return True
        return False


# 16ms, Credits - LeetCode
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        symbols = {")": "(", "}": "{", "]": "["}
        
        for c in s:
            
            if c in symbols:
                top = stack.pop() if stack else '#'
                
                if symbols[c] != top:
                    return False
            else:
                stack.append(c)
                
                
        return not stack