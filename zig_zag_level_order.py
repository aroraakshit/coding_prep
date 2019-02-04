# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # modified BFS
        if root==None:
            return []
        
        result = []
        queue = [root]
        l2r = True
        
        while(queue != []):
            s = len(queue)
            row = [0 for i in queue]
            for i in range(s):
                temp = queue[0]
                del queue[0]
                idx = i if l2r else s-1-i
                row[idx] = temp.val
                if(temp.left != None):
                    queue.append(temp.left)
                    
                if(temp.right != None):
                    queue.append(temp.right)
            l2r = not l2r
            result.append(row)
        return result