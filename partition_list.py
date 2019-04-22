# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # 40ms
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        
        init = ListNode(None)
        delete_later = init
        init.next = head
        forw = head
        
        while forw.next != None and forw.val < x:
            forw = forw.next
            init = init.next
        
        if not forw.next:
            return head
        
        while forw.next != None:
            if forw.next.val < x:
                tmp = forw.next
                forw.next = forw.next.next
                tmp.next = init.next
                if init.val == None: # new head
                    head = tmp
                init.next = tmp
                init = init.next
            else:                
                forw = forw.next
        del delete_later
        return head