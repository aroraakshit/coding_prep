class Solution(object): # 32ms, Faster than 90.71% solutions, LeetCode Medium
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.strip().split()
        ans = ''
        for i in reversed(lst):
            ans += i
            ans += ' '
        return ans.strip()

# 20ms solution, Credits - LeetCode:
class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split()
        if sl == []:
            return ''
        result = ''
        for i in range(0,len(sl)-1):
            result += sl[len(sl)-i-1]+' '
        result += sl[0]
        return result