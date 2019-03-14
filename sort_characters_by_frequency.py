class Solution: # 40ms
    def frequencySort(self, s: str) -> str:
        d = [(s.count(c),c) for c in set(s)]
        d.sort()
        l = [i*j for (i,j) in reversed(d)]
        return ''.join(l)