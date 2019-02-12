class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1): return nums[0]
        if(len(nums) % 2 == 0): 
            return False
        else:
            x = list(set(nums))
            a = sum(x) * 2
            b = sum(nums)
            return (a-b)

# Credits- LeetCode: 36ms
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        num = 0
        
        for i in range(len(nums)):
            num ^= nums[i]
            
        return num