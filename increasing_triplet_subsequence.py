# Brute force, time limit exceeded
class Solution:        
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        elif len(nums) == 3:
            return (lst[0] < lst[1] and lst[1] < lst[2])
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
            
        return False
                