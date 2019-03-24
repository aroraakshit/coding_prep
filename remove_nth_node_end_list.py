# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # 44ms
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        offset = n
        while(fast.next and offset != 0):
            fast = fast.next
            offset -= 1
        
        if offset > 1: # offset is more than length of this linkedlist
            return head
        
        if offset == 1: # we have to remove the head
            head = head.next
            return head
        
        while(fast.next):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head