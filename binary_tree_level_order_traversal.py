class Solution: # 40ms, faster than 80% solutions
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS!
        if not root:
            return []
        ans = []
        queue = [(root, 0)]
        while queue != []:
            el, level = queue[0]
            if len(ans) == level:
                ans.append([el.val])
            else:
                ans[level].append(el.val)
            queue.pop(0)
            if el.left:
                queue.append((el.left, level+1))
            if el.right:
                queue.append((el.right, level+1))
        return ans