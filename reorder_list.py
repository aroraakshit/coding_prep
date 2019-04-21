# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # 100ms, Suturing a linkedlist, Stacks
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            # if no head given
            # if first element is the last element, no need to modify
            # there are only two elements in the list, no need to modify
            return
        
        slow = head
        stack = [head]
        fast = head
        odd = False
        while True:
            slow = slow.next
            stack.append(slow)
            fast = fast.next.next
            if fast.next == None:
                odd = True
                break
            elif fast.next.next == None:
                odd = False
                break
                
        if odd:
            forward = slow.next
            slow.next = None
        else:
            forward = slow.next.next
            slow.next.next = None
        
        # i = 0
        stack.pop()
        while forward:
            backward = stack.pop()
            tmp = forward.next
            forward.next = slow
            backward.next = forward
            forward = tmp
            slow = backward
            # i += 1