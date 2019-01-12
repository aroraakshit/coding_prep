# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3_head = ListNode(0)
        l3 = l3_head
        carry = 0
        while l1 != None and l2 != None:
            l3.next = ListNode(l1.val + l2.val + carry)
            carry = l3.next.val // 10
            l3.next.val -= carry*10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
            
        if l1 == None: 
            temp = l2
        else:
            temp = l1
        
        while temp != None:
            l3.next = ListNode( temp.val + carry )
            carry = l3.next.val // 10
            l3.next.val -= carry*10
            temp = temp.next
            l3 = l3.next
        
        if carry > 0:
            l3.next = ListNode(carry)
        
        l3_head = l3_head.next
        return l3_head
        