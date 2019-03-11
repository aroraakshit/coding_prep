""" # Credits: leetCode 
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    
    def build(self, r1, c1, r2, c2, g):
        if r1 > r2 or c1 > c2:
            return None
        isLeaf = True
        val = g[r1][c1]
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if g[i][j] != val:
                    isLeaf = False
                    break
        if(isLeaf):
            return Node(val == 1, True, None, None, None, None)
        rowMid = (r1+r2) // 2
        colMid = (c1+c2) // 2
        return Node(False, False, 
                    self.build(r1, c1, rowMid, colMid, g),
                   self.build(r1, colMid+1, rowMid, c2, g),
                   self.build(rowMid+1, c1, r2, colMid, g),
                   self.build(rowMid+1, colMid + 1, r2, c2, g))
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.build(0, 0, len(grid) - 1, len(grid) - 1, grid)