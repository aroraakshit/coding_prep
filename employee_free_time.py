# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq # Credits: LeetCode, 108ms
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(schedule)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in schedule for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor,t))
            anchor = max(anchor, schedule[e_id][e_jx].end)
            if e_jx+1 < len(schedule[e_id]):
                heapq.heappush(pq, (schedule[e_id][e_jx+1].start, e_id, e_jx+1))
        return ans

class Solution(object):# credits - LeetCode
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        
        res = []
        times = [i for s in schedule for i in s]
        times.sort(key=lambda x: x.start)
        prev = times[0]
        
        for intv in times[1:]:
            if intv.start<=prev.end and intv.end>=prev.end:
                prev.end = intv.end
                
            elif intv.start > prev.end:
                res.append(Interval(prev.end, intv.start))
                prev = intv
                
        return res