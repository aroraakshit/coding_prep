from collections import defaultdict # 148ms, based on union find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # null checks
        # dim less than 2
        
        ds = defaultdict(int)
        
        for i in range(len(M)):
            for j in range(i, len(M[i])):
                if i == j:
                    if ds[i+1] == 0:
                        ds[i+1] = i+1
                    # print(i+1, j+1, ds)
                elif M[i][j] == 1:
                    if ds[i+1] == 0 and ds[j+1] == 0: # none of them have a parent
                        ds[i+1] = i+1
                        ds[j+1] = i+1
                    elif ds[i+1] == 0 or ds[j+1] == 0: # only one has a parent
                        ds[i+1] = max(ds[i+1], ds[j+1])
                        ds[j+1] = max(ds[i+1], ds[j+1])
                    else: # both have parents, merge op
                        a = ds[i+1]
                        b = ds[j+1]
                        for key in ds.keys():
                            if ds[key] == a:
                                ds[key] = b
                    # print(i+1, j+1, ds)
        return len(set(ds.values()))

class Solution: # 44ms, credits - LeetCode 
    def findCircleNum(self, M: 'List[List[int]]') -> 'int':
        count = 0
        n = len(M)
        unprocessed = set(range(len(M)))
        for i in range(n):
            if i not in unprocessed:
                continue
            count += 1
            new_friends = [i]
            unprocessed.remove(i)
            while new_friends:
                j = new_friends.pop()
                for k in list(unprocessed):
                    if M[j][k]:
                        new_friends.append(k)
                        unprocessed.remove(k)
        return count