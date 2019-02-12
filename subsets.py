class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(2 ** len(nums)):
            mask = 1
            temp = []
            for j in range(len(nums)):
                if mask & i != 0:
                    temp.append( nums[j] )
                mask = mask << 1;
            ans.append(temp)
        return ans