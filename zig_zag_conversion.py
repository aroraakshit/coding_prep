class Solution: # 100ms
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        elif numRows == 1:
            return s
        
        lst = [[] for i in range(numRows)]
        fl = True
        j = 0
        for i in range(len(s)):
            lst[j].append(s[i])
            if fl:
                j += 1
            else:
                j -= 1
                
            if j%(numRows-1) == 0 or j == 0:
                fl = not fl
        
        strings = [''.join(i) for i in lst]
        return ''.join(strings)

# but if we simply use list of strings instead of list of lists

class Solution: # 78ms
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        elif numRows == 1:
            return s
        
        lst = ['' for i in range(numRows)]
        fl = True
        j = 0
        for i in range(len(s)):
            lst[j] += s[i]
            if fl:
                j += 1
            else:
                j -= 1
                
            if j%(numRows-1) == 0 or j == 0:
                fl = not fl
        
        return ''.join(lst)