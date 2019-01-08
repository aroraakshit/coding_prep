# https://leetcode.com/problems/longest-substring-without-repeating-characters/ 
class Solution(object):
    def lengthOfLongestSubstring(self, st):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 1
        if st == '': return 0;
        
        le = [1]
        while j < len(st):
            if st[j] in st[i:j]:
                le.append(len(st[i:j]))
                while(st[i]!=st[j]):
                    i += 1
                i+=1
            j += 1
            
        le.append(len(st[i:j]))
                
        return max(le)