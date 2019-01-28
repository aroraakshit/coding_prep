# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution: # 40ms
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1        
        elif target < nums[0]:
            i = len(nums) - 1
            inc = -1
        elif target > nums[0]:
            i = 0
            inc = 1
        else:
            return 0
        
        while 0 <= i <= len(nums)-1:
            if target == nums[i]:
                return i
            i += inc
        
        return -1