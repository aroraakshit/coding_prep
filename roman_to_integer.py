class Solution: #136ms
    def romanToInt(self, s: str) -> int:
        tmp = ''
        num = 0
        for i in range(len(s)):
            if s[i] == 'I':
                num += 1
            elif i>0 and s[i-1] == 'I' and s[i] == 'V':
                num += 3
            elif s[i] == 'V':
                num += 5
            elif i>0 and s[i-1] == 'I' and s[i] == 'X':
                num += 8
            elif s[i] == 'X':
                num += 10
            elif i>0 and s[i-1] == 'X' and s[i] == 'L':
                num += 30
            elif s[i] == 'L':
                num += 50
            elif i>0 and s[i-1] == 'X' and s[i] == 'C':
                num += 80
            elif s[i] == 'C':
                num += 100
            elif i>0 and s[i-1] == 'C' and s[i] == 'D':
                num += 300
            elif s[i] == 'D':
                num += 500
            elif i>0 and s[i-1] == 'C' and s[i] == 'M':
                num += 800
            elif s[i] == 'M':
                num += 1000
        return num

class Solution: # 108ms, Credits - LeetCode
    def romanToInt(self, os: 'str') -> 'int':
        x = {'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C': 100, 'D': 500, 'M': 1000}
        s = 0
        prev = None
        cur = None
        
        for cur_s in os:
            cur = x[cur_s]
            if prev is None:
                prev = cur
            elif prev >= cur:
                s = s + prev
                prev = cur
            else:
                s = s + (cur - prev)
                prev = None
                cur = None
        if cur is not None:
            s = s + cur
        return s