class Solution: #392ms
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d = []
        for i in points:
            d.append([i, (i[0])**2 + (i[1])**2])
        d.sort(key=lambda x: x[1])
        points = [i[0] for i in d[:K]]
        return points