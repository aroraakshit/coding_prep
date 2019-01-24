# Memoizing the previous recursive solution
# works with all cases - 56ms
class Solution:
    d = {}
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # print(s1, s2, s3)
        # base cases
        if len(s1) + len(s2) != len(s3):
            return False
        elif len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        
        if s3[0] == s1[0] and s3[0] == s2[0]:
            if (s1+','+s2[1:]+','+s3[1:]) not in self.d:
                self.d[s1+','+s2[1:]+','+s3[1:]] = self.isInterleave(s1,s2[1:],s3[1:])
            if (s1[1:]+','+s2+','+s3[1:]) not in self.d:
                self.d[s1[1:]+','+s2+','+s3[1:]] = self.isInterleave(s1[1:],s2,s3[1:])
            return self.d[s1+','+s2[1:]+','+s3[1:]] or self.d[s1[1:]+','+s2+','+s3[1:]]
        elif s3[0] == s2[0]:
            if (s1+','+s2[1:]+','+s3[1:]) not in self.d:
                self.d[s1+','+s2[1:]+','+s3[1:]] = self.isInterleave(s1,s2[1:],s3[1:])
            return self.d[s1+','+s2[1:]+','+s3[1:]]
        elif s3[0] == s1[0]:
            if (s1[1:]+','+s2+','+s3[1:]) not in self.d:
                self.d[s1[1:]+','+s2+','+s3[1:]] = self.isInterleave(s1[1:],s2,s3[1:])
            return self.d[s1[1:]+','+s2+','+s3[1:]]
        else:
            return False