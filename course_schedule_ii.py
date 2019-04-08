from collections import defaultdict
class Solution: # 56ms, Topological Sort, mixed with cycle detection
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:        
        
        # build graph first
        d = defaultdict(list)
        for c,p in prerequisites:
            d[p].append(c)
        visited = [False for i in range(numCourses)]
        recStack = [False for i in range(numCourses)]
        stack = []
        
        # topological sort
        def ts(src):
            visited[src] = True
            recStack[src] = True
            for child in d[src]:
                if visited[child] == False:
                    if ts(child) == True:
                        return True
                elif recStack[child] == True:
                    return True
            stack.append(src)
            recStack[src] = False
            return False
        
        for i in range(numCourses):
            if visited[i] == False:
                if ts(i) == True:
                    return []
        
        return stack[::-1]