# 130/131 test cases passed, the last test case memory limits exceeded!, based on merge two sorted lists
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        candidates = [(lists[i].val,i) for i in range(len(lists)) if lists[i] != None]
        if candidates == []:
            return None
        min_cand, min_pos = min(candidates)
        if lists[min_pos].next == None:
            del lists[min_pos]
        else:
            lists[min_pos] = lists[min_pos].next
        head = ListNode(min_cand)
        head.next = self.mergeKLists(lists)
        return head

# 5 seconds, faster than only 9.41% solutions
import numpy as np
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if (lists == []): return 
        pos = []
        temp = []
        for l in lists:
            if(l == None or l.val == None):
                del l
                continue
            temp.append(l.val)
            pos.append(l)

        ans = ListNode(0)
        head_ans = ans
        while(len(pos) != 0):
            select_min_list = np.argmin(temp)
            ans.next = ListNode(pos[select_min_list].val)
            ans = ans.next
            if(pos[select_min_list].next == None):
                del pos[select_min_list]
                del temp[select_min_list]
            else:
                pos[select_min_list] = pos[select_min_list].next
                temp[select_min_list] = pos[select_min_list].val
        return head_ans.next

# 40ms, Credits - LeetCode, build a big list, and sort it!
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        t = []
        for node in lists:
            while node != None:
                t.append(node)
                node = node.next
        t.sort( key=lambda node: node.val)
        for i in range(len(t) - 1):
            t[i].next = t[i + 1]
        if len(t) == 0:
            return None
        return t[0]