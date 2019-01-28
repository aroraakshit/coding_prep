# https://leetcode.com/problems/rotate-image/
# 36ms solution

import math
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # Method 1 - 128 ms, but did not work because np.matrix creates a new object.
        # matrix = np.matrix(matrix)
        # matrix = matrix.transpose()
        # matrix = np.fliplr(matrix)
        # print(matrix)
        
        # Method 2: design transpose and flip functions myself
        if(len(matrix) == 1): return
        
        n = len(matrix)
        
        # transpose
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        # reverse left-right
        for i in range(n):
            for j in range(int(n/2)):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        