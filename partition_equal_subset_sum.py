class Solution: # wrong answer
    def canPartition(self, nums: 'List[int]') -> 'bool':
        if len(nums) == 1:
            return False
        # print(nums)
        nums.sort()
        i = 0
        j = len(nums)-1
        leftSum = nums[0]
        rightSum = nums[-1]
        while i<j:
            # print(nums[i:j+1])
            if leftSum == rightSum:
                break
            elif leftSum > rightSum:
                j -= 1
                rightSum += nums[j]
            elif leftSum < rightSum:
                i += 1
                leftSum += nums[i]
        
        if i==j-1 and leftSum == rightSum:
            return True
        elif i < j-1 and leftSum == rightSum:
            return True and self.canPartition(nums[i+1:j])
        else:
            return False
        
        
# fails on the case where: [1,2,3,4,5,6,7] should return True

# Credits: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation 
class Solution: #708ms
    def canPartition(self, nums: 'List[int]') -> 'bool':
        total = sum(nums)
        if total%2:
            return False
        total = total // 2
        dp = [False for i in range(total+1)]
        dp[0] = True
        for num in nums:
            for i in reversed(range(1,total+1)):
                # print(i)
                if i>=num:
                    dp[i] = dp[i] or dp[i-num]
            # print(dp)
        return dp[total]


def dfs(i, nums, target): #36ms, Credits - LeetCode
    n = nums[i]
    j = i + 1
    if n == target:
        return True
    if n > target or j == len(nums):
        return False
    return dfs(j, nums, target - n) or dfs(j, nums, target)

class Solution:
    def canPartition(self, nums):
        nums.sort(reverse=True)
        s = sum(nums)
        if s & 1: # is sum is odd
            return False
        return dfs(0, nums, s >> 1)