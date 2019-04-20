import operator
from collections import defaultdict
import math
class Solution: # 104 ms, handling duplicates took hours to resolve, defining a line was interesting!
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        line_d = defaultdict(set)
        dups = defaultdict(int)
        visited = []
        for p1 in range(len(points)):
            for p2 in range(p1+1, len(points)):
                if (points[p2][0]-points[p1][0]) == 0:
                    slope = float(math.inf)
                    tmp = points[p2][0]
                else:
                    slope = round((points[p2][1] - points[p1][1]) / (points[p2][0]-points[p1][0]), 9)
                    tmp = points[p2][1] - slope*points[p2][0]
                if points[p1][0] == points[p2][0] and points[p1][1] == points[p2][1] and p2 not in visited:
                    dups[(points[p1][0], points[p1][1])] += 1
                    visited.append(p2)
                line_d[(tmp,slope)].add((points[p1][0], points[p1][1]))
                line_d[(tmp,slope)].add((points[p2][0], points[p2][1]))

        max_count = 1
        for i in line_d.keys():
            tmp = 0
            for point in line_d[i]:
                tmp += 1 + dups[point]
            max_count = max(max_count, tmp)
        return max_count