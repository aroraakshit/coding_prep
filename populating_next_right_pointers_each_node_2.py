class Solution: # 164ms, same as my prev solution to simpler problem, faster than 90% solutions
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