# Credits LeetCode, 104ms
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        startingPoint=None
        for row in range(len(A)):
            for col in range(len(A[0])):
                #print row
                #print col
                #print "---------"
                if A[row][col] == 1:
                    startingPoint = [row, col]
                    break
        queue = []
        #print startingPoint
        #print queue
        self.dfs(startingPoint[0], startingPoint[1], queue, A)
        #print queue
        #print A
        res = 1
        while len(queue) > 0:
            curLength = len(queue)
            for i in range(curLength):
                cur = queue.pop(0)
                row = cur[0]
                column = cur[1]
                A[row][column] = -1
                if row - 1 >= 0:
                    if A[row - 1][column] == 0:
                        queue.append([row - 1, column])
                        A[row - 1][column] = -1
                    elif A[row - 1][column] == 1:
                        return res
                if row + 1 <= len(A) - 1:
                    if A[row + 1][column] == 0:
                        queue.append([row + 1, column])
                        A[row + 1][column] = -1
                    elif A[row + 1][column] == 1:
                        return res
                if column - 1 >= 0:
                    if A[row][column-1] == 0:
                        queue.append([row, column-1])
                        A[row][column-1] = -1
                    elif A[row][column-1] == 1:
                        return res
                if column + 1 <= len(A[0]) - 1:
                    if A[row][column+1] == 0:
                        queue.append([row, column+1])
                        A[row][column+1] = -1
                    elif A[row][column+1] == 1:
                        return res
            res+=1
        return res
        
    def dfs(self, row, column, queue, A):
        if A[row][column] == 1:
            A[row][column] = -1
        elif A[row][column] == -1:
            return
        elif A[row][column] == 0:
            queue.append([row, column])
            return
        if row - 1 >= 0:
            self.dfs(row - 1, column, queue, A)
        if row + 1 <= len(A) - 1:
            self.dfs(row + 1, column, queue, A)
        if column - 1 >= 0:
            self.dfs(row, column - 1, queue, A)
        if column + 1 <= len(A[0]) - 1:
            self.dfs(row, column + 1, queue, A)