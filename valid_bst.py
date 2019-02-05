import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # 52ms
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if(root == None):
            return True
        
        stack = [(root, -sys.maxsize-1, sys.maxsize)]
        
        while(stack != []):
            # print(stack[-1])
            tmp = stack.pop()
            
            if tmp[0].val < tmp[1] or tmp[0].val > tmp[2]:
                return False
            
            if tmp[0].left != None:
                stack.append((tmp[0].left, tmp[1], tmp[0].val-1))
                
            if tmp[0].right != None:
                stack.append((tmp[0].right, tmp[0].val+1, tmp[2]))
            
        return True

# In-order traversal approach , checking order!
# credits - LeetCode

# class Solution:  
    
#     def isValidBST(self, root):
#         if root == None:
#             return True
        
#         res, s = [], []
        
#         prev = -float('inf')
        
#         while len(s) or root:
#             while root:
#                 s.append(root)
#                 root = root.left
#             root = s.pop()
#             if root.val <= prev:  # if the list is not sorted
#                 return False
#             prev = root.val 
#             root = root.right
            
#         return True