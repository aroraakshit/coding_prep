# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution: #almost works
# failed at: [3,1,5,0,2,4,6,null,null,null,3]
# My output: 
# [["","","","","","","","3","","","","","","",""],["","","","1","","","","","","","","5","","",""],["","0","","","","2","","","","","4","","6","",""],["","","","","","","3","","","","","","","",""]]
# Actual output:
# [["","","","","","","","3","","","","","","",""],["","","","1","","","","","","","","5","","",""],["","0","","","","2","","","","4","","","","6",""],["","","","","","","3","","","","","","","",""]]

    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return [[]]
        left_lst = self.printTree(root.left)
        right_lst = self.printTree(root.right)
        if left_lst == [[]] and right_lst == [[]]: #no left/right child
            return [[str(root.val)]]
        else:
            b = max(len(left_lst[0]), len(right_lst[0]))
            l = max(len(left_lst), len(right_lst))
            # have both the lists conform to maximum length and breadth
            t_l = len(left_lst)
            t_b = len(left_lst[0])
            # print("left",left_lst, b,t_b)
            for i in range(l-t_l):
                left_lst += [["" for i in range(t_b)]]
            
            for i in range(len(left_lst)):
                left_lst[i] = ["" for i in range((b-t_b)//2)] + left_lst[i] + ["" for i in range(int(math.ceil((b-t_b)/2)))]
                
            t_l = len(right_lst)
            t_b = len(right_lst[0])
            # print("right",right_lst, b,t_b)
            for i in range(l-t_l):
                right_lst += [["" for i in range(t_b)]]
            for i in range(len(right_lst)):
                right_lst[i] = ["" for i in range((b-t_b)//2)] + right_lst[i] + ["" for i in range(int(math.ceil((b-t_b)/2)))]
        
        # print(left_lst,right_lst)
        # at this point both lists have equal sizes   
        final_lst = []
        root_lst = ["" for i in range(len(left_lst[0]))]
        root_lst += [str(root.val)]
        root_lst += ["" for i in range(len(right_lst[0]))]
        final_lst.append(root_lst)
        for i in range(len(right_lst)):
            final_lst.append(left_lst[i]+[""]+right_lst[i])
        # print(final_lst,"\n")
        return final_lst


# Credits: Leetcode, 44ms
class Solution:
    
    def getHeight(self, root):
        if root == None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
    def fill(self,res, root, i, l, r):
        if root == None:
            return
        res[i][(l+r)//2] = "" + str(root.val) 
        self.fill(res, root.left, i+1,l,(l+r)//2)
        self.fill(res, root.right, i+1,(l+r+1)//2,r)
    
    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = self.getHeight(root)
        res = [["" for i in range((1<<height) - 1)] for j in range(height)]
        self.fill(res, root, 0, 0, len(res[0]))
        return res