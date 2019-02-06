# idea from: https://www.youtube.com/watch?v=g8bSdXCG-lA 
# link to problem: https://leetcode.com/problems/maximal-rectangle/ 
# ideas of maximum area under histogram and DP!
# 104 ms:
def max_area_histogram(row):
    stack =[]
    max_area = 0
    index = 0
    while index < len(row):
        if(not stack) or (row[stack[-1]] <= row[index]):
            stack.append(index)
            index+=1
        else:
            top_of_stack = stack.pop() 
            area = (row[top_of_stack] * \
                   ((index - stack[-1] - 1)  \
                   if stack else index))
            max_area = max(max_area, area) 
    while stack:
        top_of_stack = stack.pop() 
        area = (row[top_of_stack] * \
              ((index - stack[-1] - 1)  \
                if stack else index))
        max_area = max(max_area, area) 
    return max_area

class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        max_so_far = 0
        row = []
        for i in range(len(matrix)):
            if row == []:
                row = [int(l) for l in matrix[i]]
            else:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == '0':
                        row[j] = 0
                    else:
                        row[j] = int(matrix[i][j]) + row[j]
            x = max_area_histogram(row)
            # print(row,x)
            max_so_far = max(x, max_so_far)
    
        return max_so_far


# more ideas, credits -  : 76ms


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans