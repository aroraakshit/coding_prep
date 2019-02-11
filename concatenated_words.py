class Solution: # TLE
    
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
    
    def findAllConcatenatedWordsInADict(self, words: 'List[str]') -> 'List[str]':
        if not words or len(words) == 1:
            return []
        lengths = list(set([len(word) for word in words]))
        if sum(lengths) == 0:
            return []
        lengths.sort()
        to_scan = []
        from_scan = []
        for i in words:
            if len(i) > lengths[0]:
                to_scan.append(i)
        
        concatenated_words = []
        for i in words:
            from_scan = [word for word in words if word!=i]
            if self.wordBreak(i, from_scan) and i!="":
                concatenated_words.append(i)
        
        return concatenated_words

class Solution: # 9960ms
    
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        dp = [False for i in range(len(s)+1)]
        wordSet = set(wordDict)
        dp[0] = True
        for i in range(1, len(s)+1):
            # print(dp)
            for j in range(i):
                # print(s[j:i])
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]
    
    def findAllConcatenatedWordsInADict(self, words: 'List[str]') -> 'List[str]':
        if not words or len(words) == 1:
            return []
        words.sort(key=lambda x: -len(x))
        concatenated_words = []
        for i in range(len(words)):
            from_scan = words[i+1:]
            if words[i]!="" and self.wordBreak(words[i], from_scan):
                concatenated_words.append(words[i])
        
        return concatenated_words

# 196ms (Credits: leetcode)
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        wset = set()
        mini = float('inf')

        for s in words:
            if not s: continue
            wset.add(s)
            mini = min(mini, len(s))

        if not wset:
            return []

        memo = {}

        def check(s):
            if s not in memo:
                memo[s] = False

                for i in range(mini, len(s) - mini + 1):
                    if s[:i] in wset:
                        t = s[i:]
                        if t in wset or check(t):
                            memo[s] = True
                            break

            return memo[s]

        return [s for s in wset if check(s)]

