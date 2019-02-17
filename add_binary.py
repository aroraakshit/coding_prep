# https://leetcode.com/problems/add-binary/

class Solution: #40ms
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        return bin( int(a,2) + int(b,2) )[2:]

class Solution: #48ms
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        (a,b) = (a,b) if len(a) > len(b) else (b,a)
        c = ''
        z = ''
        while(a!='' or b!='' or c!=''):
            a = a if len(a) > 0 else '0'
            b = b if len(b) > 0 else '0'
            c = c if len(c) > 0 else '0'
            if a[-1]+b[-1]+c == '111':
                z = '1' + z
                c = '1'
            elif (a[-1]+b[-1]+c).count('1') == 2:
                z = '0' + z
                c = '1'
            elif (a[-1]+b[-1]+c).count('1') == 1:
                z = '1' + z
                c = ''
            elif (a[-1]+b[-1]+c).count('1') == 0:
                z = '0'+z
                c = '' if c == '0' else c
            a = a[:-1]
            b = b[:-1]
        return z