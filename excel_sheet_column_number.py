class Solution: # 56ms
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in (range(len(s))):
            result = result * 26 + ord(s[i])-ord('A')+1
        
        return result