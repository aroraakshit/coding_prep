# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # 64ms
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # dfs based solution
        s = 0
        
        if not root:
            return s
        
        stack = [(root, str(root.val))]
        
        while stack != []:
            node, val = stack.pop(0)
            
            if node.left:
                stack.append((node.left, val+str(node.left.val)))
            
            if node.right:
                stack.append((node.right, val+str(node.right.val)))
            
            if not node.left and not node.right:
                s += int(val, 2)
                
        return s

# a bit quicker recursive solution and using bit manipulation, credits - LeetCode, 40ms
class Solution:
    def sumRootToLeaf(self, root: TreeNode, prevSum = 0) -> int:
        if not root: return 0
        prevSum = prevSum << 1 | root.val # cool
        if not root.left and not root.right:
            return prevSum
        return self.sumRootToLeaf(root.left, prevSum) + self.sumRootToLeaf(root.right, prevSum)
        