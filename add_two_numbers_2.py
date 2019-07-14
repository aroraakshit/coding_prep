# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # based on add two numbers first version, using stacks to reverse lists, 96ms, faster than only 14% of solutions
    def addTwoNumbers(self, l1_o, l2_o):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = []
        while(l1_o != None):
            l1.append(l1_o.val)
            l1_o = l1_o.next
        l2 = []
        while(l2_o != None):
            l2.append(l2_o.val)
            l2_o = l2_o.next
        
        l3_head = ListNode(0)
        l3 = l3_head
        carry = 0
        while l1 != [] and l2 != []:
            l3.next = ListNode(l1[-1] + l2[-1] + carry)
            carry = l3.next.val // 10
            l3.next.val -= carry*10
            l1.pop()
            l2.pop()
            l3 = l3.next
            
        if l1 == []: 
            temp = l2
        else:
            temp = l1
        
        while temp != []:
            l3.next = ListNode( temp[-1] + carry )
            carry = l3.next.val // 10
            l3.next.val -= carry*10
            temp.pop()
            l3 = l3.next
        
        if carry > 0:
            l3.next = ListNode(carry)
        
        l3_head = l3_head.next
        l3 = l3_head
        l3_o = []
        while(l3 != None):
            l3_o.append(l3.val)
            l3 = l3.next
        
        l3_final = ListNode(0)
        l3 = l3_final
        while(l3_o!=[]):
            l3.next = ListNode(l3_o[-1])
            l3 = l3.next
            l3_o.pop()
        l3_final = l3_final.next
        return l3_final

class Solution: # 56ms solution, Credits - LeetCode, builds the number, adds, then builds list back again!
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:      
        sum = self.getNumber(l1) + self.getNumber(l2)
        return self.generateList(sum)
    
    def getNumber(self, l):
        v = 0
        while l:
            v, l = v * 10 + l.val, l.next
        return v

    def generateList(self, value):
        head, after = None, None
        while value > 0:
            head = ListNode(value % 10)
            head.next, after, value = after, head, value // 10
        return head if head else ListNode(0) 