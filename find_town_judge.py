class Solution: # 1392ms -> line 8 replaced -> 104ms
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N if N <= 1 else -1
        trustees = {j for i,j in trust}
        regents = {i for i,j in trust}
        lst = list(trustees - regents)
        # if lst == [] or len(lst) > 1 or sum([trust.count([i,lst[0]]) for i in list(regents)]) != N-1: # thist last statement can be improved to the following
        if lst == [] or len(lst) > 1 or [j for i,j in trust].count(lst[0]) != N-1:
            return -1
        else:
            return lst[0]

class Solution: # 92ms, Credits - LeetCode
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        nojudges = {t[0] for t in trust}
        if len(nojudges) != N-1:
            return -1
        judge = N*(N+1)//2 - sum(nojudges)
        
        if [t[1] for t in trust].count(judge) == N-1:
            return judge
        else:
            return -1