# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution: # 40ms
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        queue = deque([(root, 0, None)])
        depth_x = None
        depth_y = None
        
        while queue:
            node, depth, parent = queue.popleft()
            if node.val == x:
                depth_x = depth
                parent_x = parent
            elif node.val == y:
                depth_y = depth
                parent_y = parent
            if depth_x and depth_y:
                return (depth_x == depth_y and parent_x != parent_y)
            if node.left:
                queue.append((node.left, depth+1, node))
            if node.right:
                queue.append((node.right, depth+1, node))
            
        if not depth_x or not depth_y:
            return False
        else:
            return (depth_x == depth_y and parent_x != parent_y)