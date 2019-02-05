class Solution: # 68ms
    def addStrings(self, num1: 'str', num2: 'str') -> 'str':
        # similar to adding two linked list numbers
        c = ''
        ans = ''
        while(num1 != '' or num2 != '' or c != ''):
            x = num1[-1] if num1 != '' else '0'
            y = num2[-1] if num2 != '' else '0'
            carry = c[-1] if c != '' else '0'
            z = int(x) + int(y) + int(carry)
            ans = str(z % 10) + ans
            c = str(z//10)
            if c == '0':
                c = ''
            if num1 != '':
                num1 = num1[:-1]
            if(num2 != ''):
                num2 = num2[:-1]
        return ans