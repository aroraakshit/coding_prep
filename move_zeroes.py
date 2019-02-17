class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        if len(nums) == 2:
            if nums[0] == 0:
                nums[0], nums[1] = nums[1], nums[0]
            return
        
        s = 0
        while(s != len(nums) and nums[s] != 0):
            s += 1
        if s == len(nums): return # no zeroes found!
        f = s+1
        while(True):
            while(f != len(nums) and nums[f] == 0):
                f += 1
            if f == len(nums): return # done!
            nums[s], nums[f] = nums[f], nums[s]
            s += 1

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Method 1 - works but 1100ms
        # i = 0
        # while( sum(nums[i:]) != 0):
        #     if (nums[i] == 0):
        #         nums.append(0)
        #         del nums[i]
        #     else:
        #         i = i + 1
        
        # Method 2 - 56 ms
        cur_idx = -1
        for i in range(len(nums)):
            if(nums[i] != 0):
                cur_idx += 1
                nums[cur_idx] = nums[i]
                if(i > cur_idx):
                    nums[i] = 0
                    
        # Method 3 - 1232ms
        # i = 0
        # cur_idx = -1
        # while(sum(nums[i:]) != 0):
        #     if(nums[i] != 0):
        #         cur_idx += 1
        #         nums[cur_idx] = nums[i]
        #         if(i > cur_idx):
        #             nums[i] = 0
        #     i = i + 1
        
        # # Method 4 - 76 ms
        # cur_idx = -1
        # for i in range(len(nums)):
        #     if(nums[i] != 0):
        #         cur_idx += 1
        #         nums[cur_idx], nums[i] = nums[i], nums[cur_idx]