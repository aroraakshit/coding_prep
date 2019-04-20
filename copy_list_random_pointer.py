"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object): # 48ms
    
    maps = {}
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        # tmp = head
        # while tmp != None:
        #     print(tmp, "next-> ", tmp.next if tmp.next else None, ", random ->", tmp.random if tmp.random else None, "\n")
        #     tmp = tmp.next
        
        head_copy = Node(head.val, head.next, head.random)
        cur = head_copy.next
        cur_parent = head_copy
        self.maps[head] = head_copy
        to_process = []
        if head.random != None:
            to_process.append(head_copy)
            
        while cur != None:
            tmp = Node(cur.val, cur.next, cur.random)
            self.maps[cur] = tmp
            cur_parent.next = tmp
            if cur.random != None:
                to_process.append(tmp)
            cur_parent = tmp
            cur = cur.next
        
        for node_idx in range(len(to_process)):
            to_process[node_idx].random = self.maps[to_process[node_idx].random]
        
        # print("\n\n NewList\n")
        # tmp = head_copy
        # while tmp != None:
        #     print(tmp, "next-> ", tmp.next if tmp.next else None, ", random ->", tmp.random if tmp.random else None, "\n")
        #     tmp = tmp.next
        
        return head_copy