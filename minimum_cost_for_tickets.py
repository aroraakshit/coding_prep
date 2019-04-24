class Solution(object): # LeetCode bug reported, idea is same as solution on line 21
    d = {}
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        print(costs)
        print(days)
        if not days:
            return 0
        
        if len(days) == 1:
            return min(costs)
        
        key = frozenset(days)
        if key not in self.d:
            self.d[key] = min(costs[0] + self.mincostTickets([i for i in days if i > days[0]], costs), 
                   costs[1] +  self.mincostTickets([i for i in days if i > 6+days[0]], costs), 
                   costs[2] +  self.mincostTickets([i for i in days if i > 19+days[0]], costs))
        # print(self.d)
        return self.d[key]

# Another solution that ran at the very least, same idea, Credits - LeetCode
from functools import lru_cache
class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)