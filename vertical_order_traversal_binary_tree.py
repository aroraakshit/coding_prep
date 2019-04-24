# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(0,0,root)])
        lst = collections.defaultdict(lambda: collections.defaultdict(list))
        while queue:
            x, y, node = queue.popleft()
            lst[x][y].append(node)
            if node.left:
                queue.append((x-1,y+1,node.left))
            if node.right:
                queue.append((x+1,y+1,node.right))
         
        ans = []
        
        for x in sorted(lst):
            report = []
            for y in sorted(lst[x]):
                report.extend(sorted(node.val for node in lst[x][y]))
                print(report)
            ans.append(report)
        return ans