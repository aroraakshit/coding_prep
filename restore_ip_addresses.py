class Solution: # 40ms
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) < 4 or len(s) > 12 or int(s) > 255255255255:
            return []
        
        addresses = []
        def backtrack(st, bits, built):
            # print(st, bits, built)
            if bits == 1:
                if int(st) <= 255 and len(str(int(st))) == len(st):
                    addresses.append(built+[st])
            else:
                i = 1
                while(i <= 3 and int(st[:i]) <= 255 and len(str(int(st[:i]))) == len(st[:i]) and len(st[i:]) > 0):
                    # print(i)
                    backtrack(st[i:], bits-1, built+[st[:i]])
                    i += 1
        
        backtrack(s, 4, [])
        return ['.'.join(i) for i in addresses]