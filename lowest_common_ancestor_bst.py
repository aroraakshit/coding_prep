class Solution: # 88ms, faster than 64% solutions
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val or (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
            return root
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else: # root.val > p and root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)