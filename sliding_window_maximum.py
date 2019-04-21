class Solution: # 104ms, Credits- LeetCode
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: return []
        reuslt = [0] * (len(nums) - k + 1)
        last_max_index = -1
        for i in range(len(nums) - k + 1):
            if last_max_index < i:
                last_max_index = i
                for j in range(i, i + k):
                    if nums[j] > nums[last_max_index]: last_max_index = j
            elif nums[last_max_index] < nums[i + k - 1]: last_max_index = i + k - 1
            reuslt[i] = nums[last_max_index]
        return reuslt