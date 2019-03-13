class Solution: # 76ms
    def leastInterval(self, t: List[str], n: int) -> int:
        if not t:
            return 0
        if n == 0:
            return len(t)
        
        ft = [(t.count(i),i) for i in set(t)]
        ft.sort()
        ans = (n+1)*ft[-1][0] - n
        tmp = 0
        k = len(ft)-1
        for i in reversed(range(len(ft)-1)):
            if ft[i][0] == ft[-1][0]:
                tmp += 1
                ans+=1
            elif ft[i][0] == ft[-1][0] - 1:
                tmp += 1
            else: # ft[i][1] < ft[0][1]
                # (n-tmp)*(ft[0][1]-1) space left/idle
                k = i
                break
    
        isl = (n-tmp)*(ft[-1][0]-1)
        while(k != len(ft)-1 and k >= 0):
            isl -= ft[k][0]
            k -= 1

        if isl >= 0:
            return ans
        else:
            return ans + abs(isl)