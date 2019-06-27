class Solution: # 36ms, faster than 96%
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        length = 0
        cur = head
        
        while(cur != None):
            cur = cur.next
            length += 1
        
        if length == 1:
            return head
        
        k = k%length

        if k == 0:
            return head
        k = length - k - 1
        cur = head
        while k > 0:
            cur = cur.next
            k -= 1
        # print(cur.val)
        newhead = cur.next
        newtail = cur
        while(cur.next != None):
            cur = cur.next
        cur.next = head
        head = newhead
        newtail.next = None
        return head