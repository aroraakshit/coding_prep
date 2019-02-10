class Solution: # 44ms
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        dp = [False for i in range(len(s)+1)]
        wordSet = wordDict
        dp[0] = True
        for i in range(1, len(s)+1):
            # print(dp)
            for j in range(i):
                # print(s[j:i])
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]