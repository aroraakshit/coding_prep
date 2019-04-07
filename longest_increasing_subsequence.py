class Solution:  # O(n^2), dynamic programming, 1984ms
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        if dp == []:
            return 0
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    dp[i] = max(dp[i], 1)
                else:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

import bisect
class Solution: # 40ms, Dynamic Programming with Binary Search, O(n logn) time and O(n) space
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [None for i in nums]
        if nums == []:
            return 0
        l = 0
        for i in range(len(nums)):
            j = bisect.bisect_left(dp, nums[i], 0, l)
            dp[j] = nums[i]
            if j == l:
                l+=1
        return l