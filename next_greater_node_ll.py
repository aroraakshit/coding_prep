class Solution: # n^2, TLE
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        
        ans = [0]
        orig = [head.val]
        cur = head.next
        while cur != None:
            if cur.val - orig[-1] > 0:
                for i in range(len(ans)):
                    if orig[i] < cur.val and ans[i] == 0:
                        ans[i] = cur.val
            ans.append(0)
            orig.append(cur.val)
            cur = cur.next
        return ans

class Solution: # 488ms, faster than only 11%, keep track of indices that are still 0!
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        
        ans = [0]
        orig = [head.val]
        cur = head.next
        indices = [0]
        while cur != None:
            if cur.val - orig[-1] > 0:
                # print(cur.val, ans, indices, orig)
                i = 0
                while i < len(indices):
                    if orig[indices[i]] < cur.val:
                        # print(orig[indices[i]], " < ", cur.val, indices, i)
                        ans[indices[i]] = cur.val
                        del indices[i]
                    else:
                        i += 1
            indices.append(len(orig))
            ans.append(0)
            orig.append(cur.val)
            cur = cur.next
        return ans


class Solution: # 276ms solution, stack based solution, exploits the fact that it will be in order, that my solution does not
  def nextLargerNodes(self, head: ListNode) -> List[int]:
    if head:
      stack, node = [head], head.next
      while node:
        while stack and stack[-1].val < node.val: 
            stack.pop().val = node.val
        stack.append(node)
        node = node.next
    for node in stack: 
        node.val = 0
    return head
 
        