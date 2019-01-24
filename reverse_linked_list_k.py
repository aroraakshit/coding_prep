# https://leetcode.com/problems/reverse-nodes-in-k-group/ 56ms

# Definition for singly-linked list. 
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        p = None
        i = 0
        
        # base case:
        temp = cur
        j = 0
        while temp!=None and j < k:
            j += 1
            temp = temp.next
            
        if j < k:
            return head
            
        while(cur != None and i < k):
            i += 1
            next = cur.next
            cur.next = p
            p = cur
            cur = next
            
        if cur != None:
            head.next = self.reverseKGroup(cur, k)
            
        head = p
        return head