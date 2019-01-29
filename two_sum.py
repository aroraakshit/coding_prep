import numpy as np

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Method 1 - 208 ms
        # x = np.argsort(nums)
        # for i in range(len(nums)):
        #         for j in list(reversed(range(i+1, len(nums)))):
        #             if(nums[x[i]] + nums[x[j]]) == target:
        #                 return [int(x[i]),int(x[j])]
        # return False
        
        # Method 2 - 92 ms
        d = {}
        for i in range(len(nums)):
            if((target - nums[i]) not in d):
                d[nums[i]] = i
            else:
                return [i, d[target - nums[i]]]