from collections import defaultdict # 28ms, faster than 99% solutions
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        if not formula:
            return ''
        stack = [defaultdict(int)]
        i = 0
        count = {}
        while(i < len(formula)-1):
            name = formula[i]
            # print(formula[i], stack)
            if name == '(':
                stack.append(defaultdict(int))
                i += 1
                continue
            
            if name == ')':
                i += 1
                num = ''
                while (i < len(formula) and formula[i].isdigit()):
                    num += formula[i]
                    i += 1
                for key in stack[-1]:
                    stack[-1][key] *= int(num)
                    stack[-2][key] = stack[-2][key] + stack[-1][key]
                stack.pop()
                continue
            
            if formula[i+1].islower():
                name += formula[i+1]
                i += 1
            
            if formula[i+1].isdigit():
                num = ''
                while (i < len(formula)-1 and formula[i+1].isdigit()):
                    num += formula[i+1]
                    i += 1
                stack[-1][name] += int(num)
            elif not name.isdigit():
                stack[-1][name] += 1
            i += 1
        if i == len(formula)-1 and formula[i].isupper():
            stack[-1][formula[i]] += 1
        count = stack[-1]  
        lst = sorted([key for key in count])
        # print(count)
        for i in range(len(lst)):
            if count[lst[i]] > 1:
                lst[i] += str(count[lst[i]])
        return ''.join(lst)
            