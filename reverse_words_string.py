class Solution(object):
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