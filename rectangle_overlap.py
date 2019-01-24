# https://leetcode.com/problems/rectangle-overlap/
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        if (max(rec1[0],rec1[2]) <= min(rec2[0],rec2[2]) or max(rec2[0],rec2[2]) <= min(rec1[0],rec1[2])) or (max(rec1[1],rec1[3]) <= min(rec2[1],rec2[3]) or max(rec2[1],rec2[3]) <= min(rec1[1],rec1[3])):
            return False
        
        return True