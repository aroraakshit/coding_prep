class Solution: # 152ms, faster than 87% solutions 
    def maxTurbulenceSize(self, lst: List[int]) -> int:
        if not lst:
            return 0
        elif len(lst) == 1:
            return 1
        elif len(lst) == 2:
            return +(lst[0] != lst[1]) + 1
        
        prev_sign = 0
        l = None
        r = None
        ans = 1
        for i in range(1, len(lst)):
            cur_sign = (lst[i] - lst[i-1])
            if prev_sign == 0 and cur_sign == 0:
                continue
            elif prev_sign*cur_sign == 0:
                if r:
                    # cur_sign is 0
                    ans = max(ans, r - l+1)
                    l = None
                    r = None
                else:
                    # prev_sign was 0
                    l = i-1
                    r = i
                prev_sign = cur_sign
            elif prev_sign*cur_sign < 0:
                prev_sign = cur_sign
                r = i
            else: 
                # prev_sign == cur_sign
                if r:
                    ans = max(ans, r - l+1)
                l = i - 1
                r = i

        if r:
            ans = max(ans, r - l+1)
        return ans