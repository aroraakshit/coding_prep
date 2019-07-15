class Solution: # 36ms, faster than 66% solutions
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

class Solution: #32ms, faster than 89% solutions
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        current = root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif (stack != []):            
                el = stack[-1]
                stack.pop()
                ans.append(el.val)
                current = el.right
            else:
                break
        return ans