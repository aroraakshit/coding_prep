# https://leetcode.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        elif len(intervals) == 1: return [intervals[0]]
        
        lst = sorted(list(intervals), key= lambda x: x.start)
        merged = []
        for i in range(len(lst)):
            if merged != [] and merged[-1].end >= lst[i].start:
                merged[-1].end = max(lst[i].end,merged[-1].end)
            else:
                merged.append(lst[i])
        return merged