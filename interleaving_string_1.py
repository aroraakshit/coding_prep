# https://leetcode.com/problems/interleaving-string/ 
# wrong solution - fails on the follwing test case
# "aa"
# "ab"
# "abaa"

# explore both possibilities. Thinking recursive now

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        if len(s1) + len(s2) != len(s3):
            return False
        elif len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        i = 0
        j = 0
        k = 0
        while k < len(s3):
            print(s3[k:], s1[i:], s2[j:])
            if (i < len(s1) and s3[k] != s1[i]) and (j < len(s2) and s3[k] != s2[j]):
                    return False
            if (i < len(s1) and s3[k] == s1[i]):
                i += 1
            else:
                j += 1    
            k+=1
        return True