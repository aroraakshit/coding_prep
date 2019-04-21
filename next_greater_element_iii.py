class Solution: # 36ms, numbers/permutations
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        d = [int(i) for i in s]
        for i in reversed(range(len(s)-1)):
            if s[i] < s[i+1]:
                # print(s[i], ' < ', s[i+1])
                tmp = sorted([num for num in d[i+1:] if num>int(s[i])])[0]
                # print(tmp)
                d[i] = tmp
                for j in range(i+1, len(d)):
                    if d[j] == tmp:
                        d[j] = int(s[i])
                        break
                # print(d)
                f = [str(k) for k in d[:i+1]]
                b = [str(k) for k in sorted(d[i+1:])]
                ans = int(''.join(f+b))
                return ans if ans < 2**31 else -1
        return -1