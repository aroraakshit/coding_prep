# https://leetcode.com/problems/maximum-subarray/
# TLE
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0],nums[1]) if (nums[0] <= 0 or nums[1] <= 0) else nums[0]+nums[1]
        
        left = 0
        right = len(nums) - 1
        sums_ = sum(nums[left:right+1])
        while left < right:
            if nums[left] < nums[right]:
                left += 1
            elif nums[right] < nums[left]:
                right -= 1
            if sums_ < sum(nums[left:right+1]):
                sums_ = sum(nums[left:right+1])
        return sums_

# 44 ms Credits - GeeksforGeeks
class Solution:

    def maxSubArray(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(a) == 0: return 0
        elif len(a) == 1: return a[0]
        
        max_so_far =a[0] 
        curr_max = a[0] 

        for i in range(1,len(a)): 
            curr_max = max(a[i], curr_max + a[i]) 
            max_so_far = max(max_so_far,curr_max) 

        return max_so_far 