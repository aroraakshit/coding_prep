# https://leetcode.com/problems/generate-parentheses/

class Solution: # 76 ms, faster than only 9% submissions, after removing useless checks: speedup to 36ms, faster than 100% submissions
    def __init__(self):
        self.memo = {0:[''],1:['()']}

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n in self.memo:
            return self.memo[n]
        else:
            lst = []
            for i in range(n):
                left = self.generateParenthesis(i)
                right = self.generateParenthesis(n-1-i)
                for j in left:
                    for k in right:
                        if '(' + j  + ')' + k not in lst: # Useless check
                            lst.append( '(' + j  + ')' + k)
                        if k + '(' + j  + ')' not in lst: # Useless check
                            lst.append(k + '(' + j  + ')')
            self.memo[n] = lst
            return self.memo[n]
                
