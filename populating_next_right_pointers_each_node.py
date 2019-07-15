class Solution: # 56ms, modified bfs
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = [(root, 0)]
        leveld = {}
        while queue != []:
            el, level = queue[0]
            queue.pop(0)
            if level not in leveld:
                el.next = None
                leveld[level] = el
            else:
                el.next = leveld[level]
                leveld[level] = el
            if el.right:
                queue.append((el.right, level+1))
            if el.left:
                queue.append((el.left, level+1))
        return root

class Solution: # 36ms, Credits - LeetCode
    def connect(self, root: 'Node') -> 'Node':
        
        curr = root
        
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        
        return curr