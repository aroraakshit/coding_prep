class Solution: # TLE
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if len(s) == 0 or len(wordDict) == 0:
            return []
        
        i = 1
        possibilities = []
        while i <= len(s):
            if s[:i] in wordDict:
                possibilities.append(i)
            i += 1
        
        if len(possibilities) == 0:
            return []
        
        final = []
        for i in possibilities:
            if(len(s[i:]) != 0):
                result = self.wordBreak(s[i:], wordDict)
                tmp = []
                for j in result:
                    tmp.append(s[:i]+" "+j)
            else:
                tmp = [s[:i]]
            final += tmp
        
        return final


# Now added memoization, it gives 120ms
from collections import defaultdict
class Solution:
    def __init__(self):
        self.memo = defaultdict(list)
    
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if len(s) == 0 or len(wordDict) == 0:
            self.memo[s] = []
            return []
        
        if s in self.memo:
            return self.memo[s]
        
        i = 1
        possibilities = []
        while i <= len(s):
            if s[:i] in wordDict:
                possibilities.append(i)
            i += 1
        
        if len(possibilities) == 0:
            self.memo[s] = []
            return []
        
        final = []
        for i in possibilities:
            if(len(s[i:]) != 0):
                result = self.wordBreak(s[i:], wordDict)
                tmp = []
                for j in result:
                    tmp.append(s[:i]+" "+j)
            else:
                tmp = [s[:i]]
            final += tmp
        
        self.memo[s] = final
        
        return final

# lets optimize it even further!, this time I limited my lookahead to max len in the dictionary and removed unnecessary checks (52ms, not so big improvement)
from collections import defaultdict
class Solution:
    def __init__(self):
        self.memo = defaultdict(list)
        self.max_len = -1
    
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if len(s) == 0 or len(wordDict) == 0:
            self.memo[s] = []
            return []
        
        if self.max_len == -1:
            self.max_len = max([len(word) for word in wordDict])
        
        i = 1
        possibilities = []
        while i <= len(s) and i<=self.max_len:
            if s[:i] in wordDict:
                possibilities.append(i)
            i += 1
        
        final = []
        for i in possibilities:
            if(len(s[i:]) != 0):
                result = self.wordBreak(s[i:], wordDict) if s[i:] not in self.memo else self.memo[s[i:]]
                tmp = []
                for j in result:
                    tmp.append(s[:i]+" "+j)
            else:
                tmp = [s[:i]]
            final += tmp
        
        self.memo[s] = final
        
        return final


# 36ms solution from optimizing the solutions above: looking up string in a set is much easier than looking up string in a list
from collections import defaultdict
class Solution:
    def __init__(self):
        self.memo = defaultdict(list)
        self.wordDict = None
        self.max_len = -1
    
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if len(s) == 0 or len(wordDict) == 0:
            self.memo[s] = []
            return []
        if self.wordDict == None:
            self.wordDict = set(wordDict)
        wordDict = self.wordDict
        if self.max_len == -1:
            self.max_len = max([len(word) for word in wordDict])
        
        i = 1
        possibilities = []
        while i <= len(s) and i<=self.max_len:
            if s[:i] in wordDict:
                possibilities.append(i)
            i += 1
        
        final = []
        for i in possibilities:
            if(len(s[i:]) != 0):
                result = self.wordBreak(s[i:], wordDict) if s[i:] not in self.memo else self.memo[s[i:]]
                tmp = []
                for j in result:
                    tmp.append(s[:i]+" "+j)
            else:
                tmp = [s[:i]]
            final += tmp
        
        self.memo[s] = final
        
        return final

# credits leetcode: 36ms solution
import functools
class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        if not s or not wordDict:
            return []
        word_dict = collections.defaultdict(set)
        for word in wordDict:
            word_dict[len(word)].add(word)
        
        valid_lengths = word_dict.keys()
        min_len = min(valid_lengths)
        
        @functools.lru_cache(None)
        def dfs(string):
            if not string:
                return [[]]
            if len(string) < min_len:
                return []
            result = []
            for valid_len, valid_words in word_dict.items():
                if len(string) >= valid_len and string[:valid_len] in valid_words:
                    result.extend([[string[:valid_len]] + x for x in dfs(string[valid_len:])])
            return result
        
        return [' '.join(word_list) for word_list in dfs(s)]