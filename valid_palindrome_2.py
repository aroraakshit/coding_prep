class Solution: #TLE
    def validPalindrome(self, s: 'str') -> 'bool':
        if s == s[::-1]:
            return True
        isPalindrome = False
        for i in range(len(s)):
            tmp = s[:i]+s[i+1:]
            isPalindrome = isPalindrome or (tmp == tmp[::-1])
        return isPalindrome

class Solution: #280ms
    def validPalindrome(self, s: 'str') -> 'bool':
        if s == s[::-1]:
            return True
        s = s.lower()
        s = list(s)
        univ = string.ascii_lowercase + "0123456789"
        s = [x for x in s if x in univ]
        if(len(s) == 0):
            return True
        
        for i in range(int(len(s)/2)):
            if(s[i] != s[len(s)-1-i]):
                break
        
        tmp1 = s[:i] + s[i+1:]
        tmp2 = s[:len(s)-1-i] + s[len(s)-i:]
        
        if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
            return True
        
        return False

# remove pre-processing and it speeds up!
class Solution: #84ms
    def validPalindrome(self, s: 'str') -> 'bool':
        if s == s[::-1]:
            return True
        
        for i in range(int(len(s)/2)):
            if(s[i] != s[len(s)-1-i]):
                break
        
        tmp1 = s[:i] + s[i+1:]
        tmp2 = s[:len(s)-1-i] + s[len(s)-i:]
        
        if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
            return True
        
        return False