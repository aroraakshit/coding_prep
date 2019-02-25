class Solution: #52ms
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        elif len(strs) == 1:
            return strs[0]
        
        minlen = min([len(s) for s in strs])
        
        if minlen == 0:
            return ''
        
        ans = ''
        for i in range(minlen):
            tmp = list(set([s[i] for s in strs]))
            if len(tmp) != 1:
                break
            ans += tmp[0]
        return ans