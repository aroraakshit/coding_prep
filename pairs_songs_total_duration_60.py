from collections import defaultdict
class Solution: # 88ms, faster than only 50% solutions
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        d = defaultdict(int)
        ans = 0
        for i in range(len(time)):
            if time[i]%60 in d:
                ans += d[time[i]%60]
            elif time[i]%60 == 0:
                ans += d[60]
            d[60-time[i]%60] += 1
        return ans

class Solution: # 60ms, Credits-LeetCode
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(int)
        for i in time:
            dic[i%60] += 1
        
        inum = 0
        for key,val in dic.items():
            if key == 30 or key == 0:
                inum += (val*(val-1))//2
            elif key < 60-key and 60-key in dic:
                inum += dic[key]*dic[60-key]
        return inum