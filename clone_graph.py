"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution: # 72ms
    def __init__(self):
        self.visited = []
        self.translate = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        head_copy = Node(node.val, [])
        self.visited.append(node)
        self.translate[node] = head_copy
        for i in node.neighbors:
            if i not in self.visited:
                n_head_copy = self.cloneGraph(i)
                head_copy.neighbors.append(n_head_copy)
            else: # visited before, has a clone somewhere s.t. you are the neighbor
                head_copy.neighbors.append(self.translate[i])
        return head_copy


from collections import deque # 36ms solution, based on BFS iterative
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        head  = Node(node.val,[])
        dic = {node:head}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for i in cur.neighbors:
                if i not in dic:
                    new_node = Node(i.val,[])
                    dic[i] = new_node
                    dic[cur].neighbors.append(new_node)
                    queue.append(i)
                else:
                    dic[cur].neighbors.append(dic[i])
        return head