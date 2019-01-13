# works perfectly!
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return ''
        elif len(s) == 1: return s
        elif len(s) == 2: return s[0] if s[0] != s[1] else s
        start = 0
        length = len(s)
        max_l = 1
        max_pali = s[0]
        low = 0
        right = 0
        for i in range(1, length): # For every point taken as centre once
            # find the longest even length palindrome
            low = i-1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > max_l:
                    start = low
                    max_l = high-low+1
                    max_pali = s[low:high+1]
                low -= 1
                high += 1
            
            # find the longest odd length palindrome
            low = i-1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > max_l:
                    start = low
                    max_l = high-low+1
                    max_pali = s[low:high+1]
                low -= 1
                high += 1
        return max_pali