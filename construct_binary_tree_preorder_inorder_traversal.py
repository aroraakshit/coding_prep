# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # 84 ms, faster than 76.98% of Python3 online submissions
    def __init__(self):
        self.idx = 0
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:        
        def buildTree1(start, end):
            if start > end:
                return None
            
            curnode = TreeNode(preorder[self.idx])
            self.idx += 1
            
            if start == end:
                return curnode
            
            idxIn = inorder.index(curnode.val)
            
            curnode.left = buildTree1(start, idxIn-1)
            curnode.right = buildTree1(idxIn+1, end)
            
            return curnode
        
        return buildTree1(0, len(inorder)-1)