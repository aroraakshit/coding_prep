# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution: # 56ms
    
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
    
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
            
        lst = sorted(list(intervals), key= lambda x: x.start)
        if newInterval.end < lst[0].start:
            lst = [newInterval] + lst
            return lst
        elif newInterval.start > lst[-1].end:
            lst += [newInterval]
            return lst
        elif newInterval.start <= lst[0].start and newInterval.end >= lst[-1].end:
            lst = [newInterval]
            return lst
        
        for i in range(len(lst)):
            if not (newInterval.end < lst[i].start or lst[i].end < newInterval.start):
                break
        if i == len(lst):
            # no overlap occurs
            lst += [newInterval]
            return lst
        else:
            # some overlap occurs!
            lst += [newInterval]
            return self.merge(lst)