class Solution: # 36ms, faster than 82% of solutions
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_ = [int(i) for i in version1.split('.')]
        version2_ = [int(i) for i in version2.split('.')]
        v1 = version1_ if len(version1_) < len(version2_) else version2_
        v2 = version2_ if len(version1_) < len(version2_) else version1_
        
        def cmp(i):
            if i == len(v1):
                if i < len(v2) and sum(v2[i:]) != 0:
                    return v2
                else: # i == len(v2), or sum(v2[i:]) == 0
                    return 0
            else:
                if v1[i] > v2[i]:
                    return v1
                elif v1[i] < v2[i]:
                    return v2
                else:
                    return cmp(i+1)
        
        res = cmp(0)
        if res == version1_:
            return 1
        elif res == version2_:
            return -1
        return 0


class Solution: # 28ms solution, Credits - LeetCode, good use of zip function, and padding the sequence!
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':        
        first = version1.split('.')
        second = version2.split('.')
        while len(first) < len(second):
            first.append("0")
        while len(second)< len(first):
            second.append("0")
        
        for a, b in zip(first, second):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        if len(first) > len(second):
            return 1
        elif len(first) < len(second):
            return -1
        else:
            return 0