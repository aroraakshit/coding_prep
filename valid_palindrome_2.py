class Solution: #TLE
    def validPalindrome(self, s: 'str') -> 'bool':
        if s == s[::-1]:
            return True
        isPalindrome = False
        for i in range(len(s)):
            tmp = s[:i]+s[i+1:]
            isPalindrome = isPalindrome or (tmp == tmp[::-1])
        return isPalindrome

