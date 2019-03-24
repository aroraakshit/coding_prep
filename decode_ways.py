class Solution: # 44ms, rule based DP, Credits - LeetCode, iterative
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]

class Solution: # Credits- LeetCode, recursive, O(n), O(n)
    def numDecodings(self, s: 'str') -> 'int':
        def helper(i):
            if i in dic:
                return dic[i]
            if i >= len(s):
                return 1
            res = 0
            if 1 <= int(s[i]) <= 9:
                res += helper(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += helper(i+2)
            dic[i] = res
            return res
        dic = {}
        return helper(0) if s else 0
