# See discussion_basic_Calculator.pdf
# porting the code to Python3

from collections import deque
class Solution: # 60ms
    def calculate(self, s: str) -> int:
        l1 = 0
        o1 = 1
        l2 = 1
        o2 = 1
        stack = deque()
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = int(c)
                while(i+1 < len(s) and s[i+1].isdigit()):
                    i += 1
                    num *= 10
                    num += int(s[i])
                # print(num)
                if o2 == 1:
                    l2 = l2*num
                else:
                    l2 = l2//num
            elif c == '(':
                stack.append(l1)                
                stack.append(o1)                
                stack.append(l2)                
                stack.append(o2)
                l1 = 0
                o1 = 1
                l2 = 1
                o2 = 1
            elif c == ')':
                num = l1 + o1 * l2
                o2 = stack.pop()
                l2 = stack.pop()
                o1 = stack.pop()
                l1 = stack.pop()
                if o2 == 1:
                    l2 = l2 * num
                else:
                    l2 = l2 // num
            elif c == '*' or c == '/':
                o2 = 1 if c=='*' else -1
            elif c == '+' or c == '-':
                l1 += o1 * l2
                o1 = 1 if c == '+' else -1
                l2 = 1
                o2 = 1
            i += 1
        return l1+o1*l2


# 48ms, cleaner solution, Credits - LeetCode
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = iter(s.replace(' ', '')+'#')
        def Helper(s, stack):
            num = 0
            op = '+'
            while True:
                c = next(s,None)
                if c == None:
                    break
                if c.isdigit():
                    num = num*10+int(c)
                elif c == '(':
                    num = Helper(s, [])
                else:
                    if op == '+':
                        stack.append(num)
                    if op == '-':
                        stack.append(-num)
                    if op == '*':
                        stack[-1] *= num
                    if op == '/':
                        stack[-1] //=num
                    num = 0
                    if c == ')':
                        return sum(stack)
                    op = c
            return sum(stack)
        
        return Helper(s, [])   