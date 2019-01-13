from collections import defaultdict
class Solution:
    
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        
        return list(ans.values())