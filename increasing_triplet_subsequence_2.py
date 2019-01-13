# Credits: Leetcode

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1,s2=float('inf'),float('inf')
        for i in nums:
            if i<=s1:
                s1=i
            elif i<=s2:
                s2=i
            else:
                return True
        return False