"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution: # 68ms
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # node = head
        # while(node):
        #     print(node.val, end=' ')
        #     node = node.next
        # print('\n')
        node = head
        while (node.next): # every node except the last
            if node.child:
                sub_head = self.flatten(node.child)
                ahead = node.next
                behind = node
                behind.next = sub_head
                sub_head.prev = behind
                while(sub_head.next):
                    sub_head = sub_head.next
                # sub_head is now sub_tail
                ahead.prev = sub_head
                sub_head.next = ahead
                node.child = None
            node = node.next
        
        # node is the last node
        if node.child:
            sub_head = self.flatten(node.child)
            node.next = sub_head
            sub_head.prev = node
            node.child = None
        return head

class Solution: # 60ms, Credits - Leetcode, iterative solution
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        res = head
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next, head.child.prev, head.child = head.child, head, None
            elif head.next == None and stack:
                node = stack.pop()
                head.next, node.prev = node, head
            head = head.next
        return res