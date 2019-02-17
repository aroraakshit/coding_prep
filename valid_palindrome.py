import string
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Method 1 - 76ms
        s = s.lower()
        s = list(s)
        univ = string.ascii_lowercase + "0123456789"
        s = [x for x in s if x in univ]
#         if(len(s) == 0):
#             return True
        
#         for i in range(int(len(s)/2)):
#             if(s[i] != s[len(s)-1-i]):
#                 return False
#          return True

        if(s == s[::-1]): #Method 2 - 56ms
            return True
        else:
            return False