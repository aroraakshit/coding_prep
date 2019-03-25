class Solution: # only passes 21/37 cases, conveniently fails on 1/6
    def fractionToDecimal(self, n: int, d: int) -> str:
        f = n/d
        i = n//d
        if f == i:
            return str(i)
        else:
            s = str(f)[2:]
            if len(set(s)) == len(s):
                return str(f)
            else:
                fs = '0.('
                j = 1
                while(j < len(s)):
                    if s[:j] == s[j:2*j]:
                        break
                    j += 1
                if j == len(s):
                    return str(f)
                else:
                    return fs+s[:j]+')'

class Solution: # 36ms, ad-hoc, credits- leetcode
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0:
            return '0'
        
        f = ''
        
        if (n < 0) ^ (d < 0):
            f += '-'
        
        dividend = abs(n)
        divisor = abs(d)
        f += str(dividend // divisor)
        rem = dividend % divisor
        if rem == 0:
            return f
        f += '.'
        m = {}
        while(rem != 0):
            # print(f)
            if rem in m:
                f = f[:m[rem]] + '(' + f[m[rem]:]
                f += ')'
                break
            m[rem] = len(f)
            rem *= 10
            f += str(rem//divisor)
            rem %= divisor
        return f