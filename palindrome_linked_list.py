class Solution: # question stated specifically O(1) memory, O(n) time, 92ms
    def isPalindrome(self, head: ListNode) -> bool:
        # get the middle of the linked list
        if head == None or head.next == None:
            return True
        sptr = head
        fptr = head
        tmp = head.next
        first = True
        while fptr.next != None and fptr.next.next != None:
            fptr = fptr.next.next
            sptr = tmp
            tmp = tmp.next
            sptr.next = head
            if first:
                first = False
                head.next = None
            head = sptr
        
        if fptr.next == None:
            sptr = sptr.next
        
        while sptr != None and tmp != None:
            if sptr.val != tmp.val:
                return False
            sptr = sptr.next
            tmp = tmp.next
        return True

# a faster version, 80ms, more concise, Credits - LeetCode
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True