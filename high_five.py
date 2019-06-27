class Solution: # 40ms, faster than 80% solutions
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        if not items:
            return []
        items.sort()
        count = 0
        current = -1
        add = 0
        ans = []
        i = len(items) - 1
        while i >= 0:
            if current == -1:
                current = items[i][0]
                print(i,current)
            count += 1
            add += items[i][1]
            i -= 1
            if count == 5:
                count = 0
                ans = [[current,add//5]] + ans
                add = 0
                while i >= 0 and items[i][0] == current:
                    i -= 1
                current = items[i][0]
        
        return ans
                
class Solution: # Credits - LeetCode, 32ms, faster than 97% solutions
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        for idx, val in items:
            heapq.heappush(d[idx], val)
            
            if len(d[idx]) > 5:
                heapq.heappop(d[idx])
        
        res = [[i, sum(d[i]) // len(d[i])] for i in sorted(d)]
        
        return res