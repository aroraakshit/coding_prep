class Solution: # 228ms
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == [] or ' ' not in s:
            return
        
        for j in range(len(s)//2):
            s[j], s[len(s)-j-1] = s[len(s)-j-1], s[j]
        prev = 0
        for i in range(len(s)):
            if s[i] == " ":
                for k in range(prev, prev+(i-prev)//2):
                    s[k], s[prev+i-k-1] = s[prev+i-k-1], s[k]
                prev = i + 1
        i += 1
        for k in range(prev, prev+(i-prev)//2):
            s[k], s[prev+i-k-1] = s[prev+i-k-1], s[k]

class Solution: # 188ms, in-place, Credits - LeetCode
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rev_word = "".join(s).split(" ")[::-1]
        s[:]= list(" ".join(rev_word))