# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution: # but this does not handle the following case:
# [[0,2],[5,10],[13,23],[24,25]]
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,25]] 
# Expected: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        a = []
        for i in range(len(A)):
            for j in range(A[i].start,A[i].end+1):
                a.append(j)
        
        common = []
        for i in range(len(B)):
            for j in range(B[i].start, B[i].end+1):
                if j in a:
                    if common == []:
                        common.append(Interval(j,j))
                    elif j == 1 + common[-1].end:
                        common[-1].end = j
                    else:
                        common.append(Interval(j,j))
                        
        return common
                        
# so how do we treat them as inclusive intervals! 
# two pointers?

class Solution: # 104 ms
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        
        a_it = 0
        b_it = 0
        common = []
        while(a_it != len(A) and b_it != len(B)):
            if A[a_it].end < B[b_it].start:
                a_it += 1
            elif B[b_it].end < A[a_it].start:
                b_it += 1
            else: # it is overlapping
                common.append(Interval( max(A[a_it].start, B[b_it].start) , min(A[a_it].end, B[b_it].end) ) )
                if A[a_it].end > B[b_it].end:
                    b_it += 1
                else:
                    a_it += 1
        return common


class Solution: #88ms, Credits - LeetCode
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        if not A and not B:
            return []
        A.extend(B)
        A.sort(key=lambda x: (x.start, x.end))
        pre_s, pre_e = A[0].start, A[0].end
        res = []
        for x in A[1:]:
            if x.start > pre_e:
                pre_s, pre_e = x.start, x.end
            elif x.end > pre_e:
                res += [Interval(x.start, pre_e)]
                pre_s, pre_e = pre_e, x.end
            else:
                res += [x]
                pre_s, pre_e = x.end, pre_e
        return res
        
        