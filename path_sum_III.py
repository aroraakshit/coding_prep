
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: #almost works
    def pathSum3(self, root, s, arr, os):
        if not root:
            return 0
        
        if root.val == s:
            print(arr+[root.val], s)
            num_paths = 1
        else:    
            num_paths = 0
            
        if root.left:
            if s == os:
                num_paths += self.pathSum3(root.left, os, [], os)
                num_paths += self.pathSum3(root.left, os - root.val, [root.val], os)
            else:
                num_paths += self.pathSum3(root.left, s - root.val, arr+[root.val], os)
        
        if root.right:
            if s == os:
                num_paths += self.pathSum3(root.right, os, [], os)
                num_paths += self.pathSum3(root.right, os - root.val, [root.val], os)
            else:
                num_paths += self.pathSum3(root.right, s - root.val, arr+[root.val], os)
            
        return num_paths
        
    def pathSum(self, root: TreeNode, s: int) -> int:
        return self.pathSum3(root, s, [], s)

class Solution: # takes about 1060ms, Credits: https://medium.com/@lenchen/leetcode-437-path-sum-iii-c5c1f6bf7d67
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        # approach: examine sum for both subtrees and remember to run 
        #           children even if there is a valid path found

        if not root:
            return 0
        return self.pathSumRecursive(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumRecursive(self, root, sum):
        if not root:
            return 0

        return (1 if root.val == sum else 0) + self.pathSumRecursive(root.left, sum - root.val) + self.pathSumRecursive(root.right, sum - root.val)

class Solution:  # 60ms, credits - LeetCode  
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        
        res, targetSum = 0, sum
            
        def pathSumUtil(node, runningSum, mem):
                                    
            nonlocal res, targetSum
            
            runningSum += node.val
            complement = runningSum - targetSum
            res += mem.get(complement, 0)
            mem[runningSum] = mem.get(runningSum, 0) + 1
            if node.left:
                pathSumUtil(node.left, runningSum, mem)
            if node.right:
                pathSumUtil(node.right, runningSum, mem)
            # Backtracking, so remove pathSum
            mem[runningSum] -= 1
         
        if not root:
            return 0
        
        mem = {0: 1}
        pathSumUtil(root, 0, mem)
        
        return res