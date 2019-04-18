class Solution2(object): # Credits - LeetCode, 52ms
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]
    
class Solution: # Credits - LeetCode, 28ms
    def decodeString(self, s: 'str') -> 'str':
        def group(a):
            num = ''
            i = 0
            while i < len(a) and a[i] in '0123456789':
                num += a[i]
                i += 1
            num = int(num)
            
            j = i+1
            count = 1
            while j < len(a) and count > 0:
                if a[j] == '[':
                    count += 1
                elif a[j] == ']':
                    count -= 1
                j += 1
            
            return num, i, j-1
                
        
        res = ''
        while s:
            cur = s[0]
            if cur in '0123456789':
                num, i, j = group(s)
                res += self.decodeString(s[i+1:j])*num
                s = s[j+1:]
            else:
                res += cur
                s = s[1:]
        return res