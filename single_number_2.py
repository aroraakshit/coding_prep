class Solution(object): # 20ms
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        s = set(nums)
        a = sum(s)*3
        b = sum(nums)
        # print(s,b,a)
        return (a-b)//2


# Credits: leetcode, 24ms but constant space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones
        return ones