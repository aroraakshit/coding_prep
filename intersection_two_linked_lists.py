# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object): # hash table approach / 192ms, Faster than 80% solutions / O(m+n) time, O(m) or O(n) space complexity
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if not headA or not headB:
            return None
        
        tA = headA
        sA = []
        while tA != None:
            sA.append(tA)
            tA = tA.next
            
        tB = headB
        sB = []
        while tB != None:
            sB.append(tB)
            tB = tB.next
        
        # 3 possibilities:
            # 1) intersection somewhere in the middle... done!
            # 2) intersection at tail... done!
            # 3) intersection at head... done!
        
        pA = sA[-1]
        pB = sB[-1]
        if pA != pB:
            return None
        sA.pop()
        sB.pop()
        while sB != [] and sA != []:
            if sA[-1] != sB[-1]:
                return pA
            pA = sA[-1]
            pB = sB[-1]
            sA.pop()
            sB.pop()
        if pA == pB:
            return pA
        
        return None
 
class Solution(object): # 160ms, Credits - LeetCode
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            else:
                headB = headB.next
        return None

# Approach 3: Two Pointers (O(M+N) time, O(1) space)
# Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
# When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pBpB reaches the end of a list, redirect it the head of A.
# If at any point pApA meets pBpB, then pApA/pBpB is the intersection node.
# To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), pBpB would reach the end of the merged list first, because pBpB traverses exactly 2 nodes less than pApA does. By redirecting pBpB to head A, and pApA to head B, we now ask pBpB to travel exactly 2 more nodes than pApA would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.
# If two lists have intersection, then their last nodes must be the same one. So when pApA/pBpB reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.