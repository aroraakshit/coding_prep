# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # 80ms, faster than 97.99% percent solutions
    
    def min_right(self, p):
        if p.right:
            cur = p.right
            while cur.left:
                cur = cur.left
            return cur
        return None
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not p or not root:
            return None
        
        if p == root:
            return self.min_right(p)
        
        if p.right:
            return self.min_right(p)
        
        cur = root
        stack = []
        while cur and cur.left != p and cur.right != p:
            stack.append(cur)
            if p.val > cur.val:
                cur = cur.right
            elif p.val < cur.val:
                cur = cur.left
               
        if cur == None: # could not find p
            return None
            
        if cur.left == p:
            return cur
        
        prev = p
        while stack and cur.right == prev:
            prev = cur
            cur = stack.pop()
        
        if not stack and cur.right == prev:
            return None
        
        return cur
        