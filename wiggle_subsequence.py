 class Solution: # 36ms, Credits - LeetCode (Java), Greedy Algorithm
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        pdiff = nums[1] - nums[0]
        count = 2 if pdiff != 0 else 1
        for i in range(2,len(nums)):
            d = nums[i] - nums[i-1]
            if (d > 0 and pdiff <= 0) or (d < 0 and pdiff >= 0):
                count += 1
                pdiff = d
        return count