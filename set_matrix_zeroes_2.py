class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # solution that uses constant space
        
        i = 0 # rows
        j = 0 # cols
        flag = False
        
        # row major traversal
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if matrix[i][j] == 0 and not flag:
                    flag = True
                    matrix[i][j] = 'a'
                    j = -1
                elif flag:
                    if matrix[i][j] == 0: # if it was already set to zero, another bomb!
                        matrix[i][j] = 'a'
                    elif matrix[i][j] != 'a':
                        matrix[i][j] = 0
                j += 1
            flag = False
            i += 1
        print(matrix)
        # column major traversal
        j = 0
        flag = False
        while j < len(matrix[0]):
            i = 0
            while i < len(matrix):
                # print("i",i,"j",j)
                if matrix[i][j] == "a" and not flag:
                    flag = True
                    i = -1
                elif flag:
                    matrix[i][j] = 0
                i += 1
            flag = False
            j += 1