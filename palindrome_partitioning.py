class Solution: # 108ms, Credits - LeetCode
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]


# Pre-selecting starting points for DFS instead of checking isPal every single time: Credits - LeetCode, 68ms
from collections import defaultdict
class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        strLength = len(s)
        dp_array = defaultdict(set)
        res = []
        for i in range(strLength):
            j = i
            k = i
            while j >= 0 and k < strLength and s[j] == s[k]:
                dp_array[j].add(k)
                j -= 1
                k += 1
            j = i
            k = i + 1
            while j >= 0 and k < strLength and s[j] == s[k]:
                dp_array[j].add(k)
                j -= 1
                k += 1
        self.dfs(0, [], strLength, res, dp_array, s)
        return res


    def dfs(self, i, tempres, strLength, res, dp_array, s):
        for j in dp_array[i]:
            if j + 1 == strLength:
                res.append(tempres + [s[i:j+1]])
            else:
                self.dfs(j+1, tempres + [s[i:j+1]], strLength, res, dp_array, s)
        
