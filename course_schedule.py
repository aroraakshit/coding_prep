from collections import defaultdict

class Solution: # 48ms, Cycle detection in directed graph - https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
    def __init__(self):
        self.d = defaultdict(list)
        
    def isCycleUtil(self, v, visited, recStack):
        # print(v, visited, recStack)
        visited[v] = True
        recStack[v] = True
        for nbr in self.d[v]:
            if visited[nbr] == False:
                if self.isCycleUtil(nbr, visited, recStack) == True:
                    return True
            elif recStack[nbr] == True:
                return True

        recStack[v] = False
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for c,p in prerequisites:
            self.d[p].append(c) # an edge from pre requisite to course
        # print(self.d)
        
        visited = [False for i in range(numCourses)]
        recStack = [False for i in range(numCourses)]
        for node in range(numCourses):
            if visited[node] == False: 
                if self.isCycleUtil(node,visited,recStack) == True:
                    return False
        return True